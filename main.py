import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from audio_utils import extract_audio_from_youtube_video, extract_youtube_id
from config import Config
from convert_audio_to_text import recognize_speech
from database_utils import add_summary_to_database, get_summary_from_database
from text_summarizer import get_summary

app = FastAPI()

OUTPUT_PATH = '/tmp/'

try:
    Config.validate_environment_variables()
except ValueError as e:
    raise HTTPException(status_code=500, detail=f'Configuration error: {e}')


class UserRequest(BaseModel):
    youtube_url: str


@app.post('/summarise/')
async def summarize_video(request: UserRequest):
    try:
        video_url = request.youtube_url
        youtube_id = extract_youtube_id(video_url)
        summary = get_summary_from_database(youtube_id)

        if summary is None:
            if not os.path.exists(OUTPUT_PATH):
                os.makedirs(OUTPUT_PATH)

            audio_path = extract_audio_from_youtube_video(url=video_url, output_path=OUTPUT_PATH)
            raw_text = recognize_speech(audio_path)
            os.remove(audio_path)
            summary = get_summary(raw_text)
            add_summary_to_database(youtube_id=youtube_id, summary=summary)

        return {'summary': summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'An error occurred during summarization: {str(e)}')


async def test_summarize_video(video_url: str) -> None:
    request = UserRequest(youtube_url=video_url)
    summary = await summarize_video(request)
    print(summary)

# import asyncio
# asyncio.run(test_summarize_video(video_url=''))
