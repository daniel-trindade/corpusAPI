from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
    
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
    
def get_video_transcript(video_id, language):
    
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])

    formatter = TextFormatter()
    text_formatted = formatter.format_transcript(transcript)

    return text_formatted

def translate_video_transcript(video_id, source_language_code, target_language_code):
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    transcript = transcript_list.find_transcript([source_language_code])
    translated_transcript = transcript.translate(target_language_code)

    translated_transcript = translated_transcript.fetch() #transforma em diciionario

    formatter = TextFormatter()
    text_formatted = formatter.format_transcript(translated_transcript)

    return text_formatted