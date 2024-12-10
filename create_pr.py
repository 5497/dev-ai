import requests
import json
import os

def create_pull_request(repo, branch, token):
    url = f"https://api.github.com/repos/{repo}/pulls"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "title": "Add generated workflow",
        "head": branch,
        "base": "main",
        "body": "This PR adds a new GitHub Actions workflow."
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        print("Pull request created successfully.")
    else:
        print(f"Failed to create pull request: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    repo = "your-username/your-repo"
    branch = "your-branch"
    token = os.getenv("GITHUB_TOKEN")
    create_pull_request(repo, branch, token)
