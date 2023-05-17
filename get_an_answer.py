import sys 
import openai
import os 

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = "org-s4rJCaE9z34iogawHXAZvckL"


chat_completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are the best research assistant in the world."},
        {"role": "user", "content": sys.argv[1]}
       
    ]
)

print(chat_completion.choices[0].message.content)
