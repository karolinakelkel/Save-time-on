from openai import OpenAI
from logger import logger

MODEL_VERSION = 'gpt-4'
ROLE = 'user'
PROMPT = ('Summarise in English and correct grammar (if needed). Do not mention the text or transcript.'
          'A summary must be really short. Only main ideas. 10 sentences max.')
TEMPERATURE = 0.7


def summarise(input_text: str, client: OpenAI) -> str:
    """
    Generates a short summary from input text using the OpenAI GPT model.

    Args:
        input_text (str): The text to summarise.
        client (OpenAI): An authenticated OpenAI client.

    Returns:
        str: The generated summary.
    """

    message_params = {'role': ROLE,
                      'content': f'{PROMPT}\n\nText:\n{input_text}\n\nSummary:'}

    try:
        response = client.chat.completions.create(model=MODEL_VERSION,
                                                  messages=[message_params],
                                                  temperature=TEMPERATURE)

        return response.choices[0].message.content.strip()

    except Exception as e:
        logger.error(f'Failed to generate summary: {e}')

        raise RuntimeError(f'Failed to generate summary: {e}')
