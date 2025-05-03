import whisper
from logger import logger

MODEL_VERSION = 'base'
RESULT_TEXT_KEY = 'text'


def recognise_speech(audio_path: str) -> str:
    """
    Transcribes speech from an audio file using the Whisper model.

    Args:
        audio_path (str): Path to the input audio file.

    Returns:
        str: Recognised text from the audio.
    """

    model = whisper.load_model(MODEL_VERSION)

    result = whisper.transcribe(model, audio_path)

    text = result[RESULT_TEXT_KEY]

    logger.info(f'Transcription completed from: {audio_path}')

    return text
