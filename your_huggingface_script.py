from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')
response = generator("Hello, how can I assist you today?", max_length=50)
print(response[0]['generated_text'])
