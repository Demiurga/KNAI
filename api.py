import openai

openai.api_key = "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"
model_engine = "text-davinci-003"


def request(data):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=data.prompt,
        max_tokens=data.max_tokens,
        temperature=data.temperature,
        top_p=1,
        frequency_penalty=data.frequency_penalty,
        presence_penalty=data.presence_penalty
    )

    return completion.choices[0].text
