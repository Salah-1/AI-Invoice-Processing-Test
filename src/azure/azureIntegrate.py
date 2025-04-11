# under construction 
# under construction 
# under construction 

# under construction 
# under construction 
# just sanity checks....

import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']


from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-3.5",
    input="What time is it? ET zone."
)

print(response.output_text)