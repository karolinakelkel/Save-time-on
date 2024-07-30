import os
from yt_dlp import YoutubeDL


def extract_audio_from_youtube(url, output_path):
    try:
        # Загрузка видео с YouTube
        print("Начинается загрузка видео...")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
        }

        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', None)
            wav_file = os.path.join(output_path, f"{title}.wav")
            print(f"Скачанный и конвертированный аудио файл: {wav_file}")

        return wav_file
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


wav_file_path = extract_audio_from_youtube('https://www.youtube.com/watch?v=rxMCuwbYje', '/Save-time-on')
if wav_file_path:
    print(f"WAV файл сохранен по пути: {wav_file_path}")
else:
    print("Не удалось создать WAV файл")
