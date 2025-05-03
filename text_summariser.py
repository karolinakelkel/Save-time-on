from openai import OpenAI
from config import Config

MODEL_VERSION = 'gpt-4'
ROLE = 'user'
PROMPT = ('Summarise in English and correct grammar (if needed). A summary must be really short. '
          'Only main ideas. 10 sentences max.')

config = Config()
client = OpenAI(api_key=config.openai_api_key)


def get_summary(input_text: str) -> str:
    """
    Generates a short summary from input text using the OpenAI GPT model.

    Args:
        input_text (str): The text to summarise.

    Returns:
        str: The generated summary.
    """

    response = client.chat.completions.create(model=MODEL_VERSION,
                                              messages=[{'role': ROLE,
                                                         'content': f'{PROMPT}\n\n'
                                                                    f'Text:\n{input_text}\n\n'
                                                                    f'Summary:'}],
                                              temperature=0.7)

    return response.choices[0].message.content.strip()
