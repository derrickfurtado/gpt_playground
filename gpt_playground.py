import openai
import config
from openai import OpenAI
from pdb import set_trace
from key import gpt_api_key


openai.api_key = gpt_api_key



def generate_text(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=10,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

prompt = "Once upon a time"


generated_text = generate_text(prompt)


print(prompt, generated_text)