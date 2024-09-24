import openai
import config
from openai import OpenAI
from pdb import set_trace
from key import gpt_api_key


client = OpenAI()
completion = client.chat.completions.create()



def generate_text(prompt):
    response = openai.completions.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=10,
        temperature=0.7
    )
    return response.choices[0].text.strip()

prompt = "Once upon a time"


generated_text = generate_text(prompt)


print(prompt, generated_text)