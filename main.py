import os
from config import Config
from openai import OpenAI
from audio_utils import extract_audio_from_youtube_video
from convert_audio_to_text import recognise_speech
from text_summariser import get_summary
from logger import logger

OUTPUT_PATH = '/tmp'

def main():
    try:
        config = Config()
        client = OpenAI(api_key=config.openai_api_key)

        video_url = input('Enter YouTube video URL: ')

        os.makedirs(OUTPUT_PATH, exist_ok=True)

        logger.info('Starting YouTube summarisation process.')
        audio_path = extract_audio_from_youtube_video(url=video_url,
                                                      output_path=OUTPUT_PATH,
                                                      ffmpeg_path=config.ffmpeg_path)
        logger.info('Audio extracted successfully.')

        raw_text = recognise_speech(audio_path)
        logger.info('Transcription completed.')

        os.remove(audio_path)

        summary = get_summary(raw_text, client)
        logger.info(f'Summary generated: {summary}')

        print(f'\n{summary}\n')
    except Exception as e:
        logger.error(f'Error occurred: {e}')
        print(f'\nError occurred: {e}')

if __name__ == '__main__':
    main()