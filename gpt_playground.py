import openai
from pdb import set_trace
from key import gpt_api_key


openai.api_key = gpt_api_key



def generate_text(prompt, max_tokens, temperature):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,                                  ### sets the limits for the number of tokens to be returned
        temperature=temperature                                 ### sets the complexity of the returned response
    )
    return response.choices[0].message.content.strip()

prompt = "Once upon a time"


generated_text = generate_text(prompt, 50, 1)


print(prompt, generated_text)