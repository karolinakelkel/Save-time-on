# from youtube_utils import extract_audio_from_youtube_video, extract_youtube_id
# from transcriber import recognize_speech
# from summarizer import get_summary
# from database_utils import add_summary_to_database, get_summary_from_database
#
# def main(url):
#     youtube_id = extract_youtube_id(url)
#     if not youtube_id:
#         print("Invalid YouTube URL")
#         return
#
#     summary_from_db = get_summary_from_database(youtube_id)
#     if summary_from_db:
#         print("Summary from database:", summary_from_db)
#         return
#
#     audio_path = extract_audio_from_youtube_video(url, "/path/to/output")
#     text = recognize_speech(audio_path)
#     summary = get_summary(text)
#     add_summary_to_database(youtube_id, summary)
#
#     print("Generated Summary:", summary)
#
# if __name__ == "__main__":
#     youtube_url = "https://www.youtube.com/watch?v=example"
#     main(youtube_url)









#
# output_path = '/Users/carolinakelkel/Save-time-on'
# wav_file_path = extract_audio_from_youtube_video('https://www.youtube.com/watch?v=B0VeKPwUY0c', output_path)
# URL = 'https://www.youtube.com/watch?v=B0VeKPwUY0c&t=1s'
# SUMMARY = 'Исследование показывает, что при отмене антидепрессантов от 26 до 60% пациентов испытывают синдром отмены, ' \
#           'однако значительная часть испытывают его и при отмене плацебо. Это подчеркивает важность постепенного ' \
#           'снижения дозировки и грамотного подхода к лечению. Врачи должны учитывать эту информацию, ' \
#           'чтобы предотвратить дискомфорт у пациентов. '
# video_id = extract_youtube_id(URL)
# add_summary_to_database(video_id, SUMMARY)