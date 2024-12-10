from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

prompt = "Explain how generative AI can be used in software development:"
response = generator(
    prompt,
    max_length=100,
    truncation=True,
    temperature=0.7,
    top_p=0.9
)

print(response[0]['generated_text'])
