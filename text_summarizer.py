import openai
import os
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_VERSION = 'gpt-4'
ROLE = 'user'
# LONG_PROMPT = 'Summarize in English and correct grammar (if needed) the following text extracted from a YouTube ' \
#               'video. Only main ideas.'
SHORT_PROMPT = 'Summarize in English and correct grammar (if needed) the following text extracted from a YouTube ' \
               'video. A summary must be really short. Only main ideas. 3 sentences max.'


def get_summary(input_text):
    client = OpenAI()
    # prompt = SHORT_PROMPT if short else LONG_PROMPT
    prompt = SHORT_PROMPT
    response = client.chat.completions.create(model=MODEL_VERSION,
                                              messages=[{'role': ROLE,
                                                         'content': f'{prompt}\n\nText:\n\n{input_text}\n\nSummary:'}],
                                              stream=True)

    summary = ''

    for chunk in response:
        if not chunk.choices:
            continue
        content = chunk.choices[0].delta.content
        if content is not None:
            summary += content

    return summary


openai.api_key = OPENAI_API_KEY
