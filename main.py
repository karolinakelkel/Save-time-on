import os
from openai import OpenAI
from config import Config
from audio_utils import extract_audio_from_youtube_video
from convert_audio_to_text import recognise_speech
from text_summariser import summarise
from logger import logger

TEMP_DIR = '/tmp'


def get_video_url_from_user() -> str:
    """
    Prompts the user to enter a YouTube video URL.

    Returns:
        str: The entered URL.
    """

    return input('Enter YouTube video URL: ')


def main() -> None:
    try:
        config = Config()
        client = OpenAI(api_key=config.openai_api_key)

        video_url = get_video_url_from_user()

        os.makedirs(TEMP_DIR, exist_ok=True)

        logger.info('Starting YouTube summarisation process.')
        audio_path = extract_audio_from_youtube_video(url=video_url,
                                                      output_path=TEMP_DIR,
                                                      ffmpeg_path=config.ffmpeg_path)
        logger.info('Audio extracted successfully.')

        raw_text = recognise_speech(audio_path)
        logger.info('Transcription completed.')

        os.remove(audio_path)

        summary = summarise(raw_text, client)
        logger.info(f'Summary generated')

        print(f'\n{summary}\n')
    except Exception as e:
        logger.error(f'Error occurred: {e}')
        print(f'\nError occurred: {e}')

if __name__ == '__main__':
    main()