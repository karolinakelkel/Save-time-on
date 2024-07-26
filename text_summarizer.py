from openai import OpenAI
import openai
import os


def get_api_key():
    return os.getenv("OPENAI_API_KEY")


def check_api_key(key: str):
    if key is None:
        raise ValueError("API key for OpenAI not found. Make sure to set the OPENAI_API_KEY environment variable.")


def summarize_text(text, language):
    client = OpenAI()

    completion = client.completions.create(model='gpt-3.5-turbo-instruct',
                                           prompt=f"Shortly summarize in {language} the following text extracted from "
                                                  f"a youtube video. One sentence. Text:\n\n{text}\n\nSummary:",
                                           max_tokens=100,
                                           temperature=0.8)
    return completion.choices[0].text


api_key = get_api_key()
check_api_key(api_key)
openai.api_key = api_key


input_text = """Скажите знакомо ли вам такое явление как спам? Знаете что это такое? Согласен, странно звучит из моих 
уст. Каждый цивилизованный человек ежедневно сталкивается со спам звонками, спам сообщениями в соцсетях, спам рассылкой 
на электронную почту и так далее. Но что, если я вам скажу, что у вас есть собственный генератор спама, который 
находится у вас прямо в голове? Меня зовут Игорь Семениченко. Я практикующий дипломированный психолог и работаю в 
основном в рамках когнитивно-поведенческой, метакогнитивной и схема терапии. Так вот основоположник метакогнитивной 
терапии Адриан Уэллс как-то раз заметил, что всем здоровым людям приходит в голову множество мыслей, в том числе 
негативных. По некоторым подсчётам от двух-трёх тысяч мыслей в сутки. Некоторые из них произвольные. Вот что заметил 
Эдриан Уэлс, что одних людей эти мысли приводят к депрессивному расстройству, к тревожному расстройству, и к прочим 
неприятным состояниям нездоровым. А кого-то не приводят. Как вы думаете почему?
"""
summarized_text = summarize_text(input_text, 'russian').strip()
print("Summarized Text:\n")
print(summarized_text)
