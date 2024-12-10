import os
import argparse

def create_workflow_file(workflow_name, branch_name, job_name, script_name):
    workflow_content = f"""
name: {workflow_name}

on:
  push:
    branches:
      - {branch_name}

jobs:
  {job_name}:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install transformers torch

    - name: Run script
      run: |
        python {script_name}
    """
    with open('.github/workflows/generated_workflow.yml', 'w') as file:
        file.write(workflow_content)

def main():
    parser = argparse.ArgumentParser(description="Generate a GitHub Actions workflow file")
    parser.add_argument('workflow_name', type=str, help='The name of the workflow')
    parser.add_argument('branch_name', type=str, help='The branch to trigger the workflow')
    parser.add_argument('job_name', type=str, help='The name of the job')
    parser.add_argument('script_name', type=str, help='The script to run in the workflow')
    args = parser.parse_args()

    create_workflow_file(args.workflow_name, args.branch_name, args.job_name, args.script_name)
    print("Workflow file created successfully.")

if __name__ == "__main__":
    main()
