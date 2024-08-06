import whisper

MODEL_VERSION = 'base'
RESULT_TEXT_KEY = 'text'


def recognize_speech(audio_path):
    model = whisper.load_model(MODEL_VERSION)

    result = model.transcribe(audio_path)

    text = result[RESULT_TEXT_KEY]

    return text
