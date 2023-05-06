import openai

openai.api_key = "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"
model_engine = "text-davinci-003"
prompt = input()

completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

print(completion.choices[0].text)
