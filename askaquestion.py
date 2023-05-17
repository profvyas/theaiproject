import requests
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = "org-s4rJCaE9z34iogawHXAZvckL"

chat_completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Where does arabica coffee originate from?"}
       
    ]
)
print(chat_completion)


