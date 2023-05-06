import openai
import textract

file_name = "dsf.docx"
encoding = "utf-8"
data = ''
text = textract.process(file_name).decode(encoding)
openai.api_key = "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"
model_engine = "text-davinci-003"
option = ''


def request(data, tokens):
    global option
    if option != '':
        option = 'В стиле ' + option
    completion = openai.Completion.create(
        engine=model_engine,
        prompt='Привет, можешь, пожалуйста, выделить самое главное в этом тексте : ' + data + '.' + option,
        max_tokens=tokens,  # по сути, от 256 до 4096
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return completion.choices[0].text


data = text
print(request(data, tokens=2048))
