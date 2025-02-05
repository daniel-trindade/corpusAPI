from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

import os

from handlers import generate_random_string, save_file

def list_languages(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        language_list = []

        for transcript in transcript_list:
            language_list.append(
                {
                    "language": transcript.language,
                    "language_code": transcript.language_code
                }
            )

        return language_list
    except:
        return []
    
def get_video_transcript(video_id, language, doc_type = "txt"):
    
    save_path = "files/"
    file_name = generate_random_string()

    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])

    formatter = TextFormatter()
    text_formatted = formatter.format_transcript(transcript)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = os.path.join(save_path, f"{file_name}.{doc_type}")
    
    save_file(file_path, text_formatted, doc_type)

    return file_path

def translate_video_transcript(video_id, source_language_code, target_language_code, doc_type = "txt"):

    save_path = "files/"
    file_name = generate_random_string()

    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    transcript = transcript_list.find_transcript([source_language_code])
    translated_transcript = transcript.translate(target_language_code)

    translated_transcript = translated_transcript.fetch() #transforma em diciionario

    formatter = TextFormatter()
    text_formatted = formatter.format_transcript(translated_transcript)

    file_path = os.path.join(save_path, f"{file_name}.{doc_type}")
    save_file(file_path, text_formatted, doc_type)

    return file_path

