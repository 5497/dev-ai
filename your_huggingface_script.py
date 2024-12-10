from transformers import pipeline
import argparse

def generate_text(prompt):
    generator = pipeline('text-generation', model='gpt2')
    response = generator(
        prompt,
        max_length=100,
        truncation=True,
        temperature=0.7,
        top_p=0.9
    )
    return response[0]['generated_text']

def main(prompt):
    generated_text = generate_text(prompt)
    print(f"Prompt: {prompt}\nGenerated Text: {generated_text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate text using Hugging Face GPT-2")
    parser.add_argument('prompt', type=str, help='The prompt to generate text from')
    args = parser.parse_args()
    main(args.prompt)
