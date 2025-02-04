from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_video_transcript(video_id):

    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt'])

    formatter = TextFormatter()
    text_formatted = formatter.format_transcript(transcript)

    return text_formatted
