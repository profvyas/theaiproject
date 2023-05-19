import requests
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = "org-s4rJCaE9z34iogawHXAZvckL"

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_streamed(prompt, model="gpt-3.5-turbo"):
    # gets completion for user propt and streams the output word by word
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
        stream=True
    )
    for chunk in response:  # this will stream the results as they come in
        chunk_message = chunk['choices'][0]['delta']
        print(chunk_message.get('content'), end = "")   # this will print the output word by word  
    return True


    