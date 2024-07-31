import whisper


def recognize_speech(audio_path):
    model = whisper.load_model('base')

    result = model.transcribe(audio_path)

    text = result['text']
    print(text)
    return text


recognize_speech('/Users/carolinakelkel/Save-time-on/31-07-2024_10-08-04_a3f203694029497ab5d2705b8db7aa10.wav')