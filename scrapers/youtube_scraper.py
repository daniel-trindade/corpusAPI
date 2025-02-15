from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

import os

from handlers import generate_random_string, save_file

def list_languages(video_id):
    """
    Lists the available transcript languages for a given YouTube video.

    Parameters
    ----------
    video_id : str
        The unique identifier of the YouTube video.

    Returns
    -------
    language_list : list
        A list of dictionaries containing available languages and their corresponding language codes.

    Notes
    -----
    - Each dictionary in the list has the keys `"language"` (full language name) and `"language_code"` (ISO code).
    - If no transcripts are available or an error occurs, an empty list is returned.
    """
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
    """
    Retrieves and saves the transcript of a YouTube video in the specified format.

    Parameters
    ----------
    video_id : str
        The unique identifier of the YouTube video.
    language : str
        The language code for the desired transcript.
    doc_type : str, optional
        File format for saving the transcript (default: "txt").

    Returns
    -------
    file_path : str
        Path to the saved file containing the video transcript.

    Notes
    -----
    - The transcript is retrieved using `YouTubeTranscriptApi`.
    - The text is formatted before being saved.
    - The output file name is generated randomly.
    - The file is saved in the "files/" directory.
    - If the directory does not exist, it is created automatically.
    """
    
    save_path = "files/"
    file_name = generate_random_string()

    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])

    formatter = TextFormatter()
    text_formatted = formatter.format_transcript(transcript)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = os.path.join(save_path, f"{file_name}.{doc_type}")
    
    save_file(file_path, text_formatted.replace('\n', ' '), doc_type)

    return file_path

def translate_video_transcript(video_id, source_language_code, target_language_code, doc_type = "txt"):
    """
    Translates the transcript of a YouTube video and saves it in the specified format.

    Parameters
    ----------
    video_id : str
        The unique identifier of the YouTube video.
    source_language_code : str
        The language code of the original transcript.
    target_language_code : str
        The language code for the translation.
    doc_type : str, optional
        File format for saving the translated transcript (default: "txt").

    Returns
    -------
    file_path : str
        Path to the saved file containing the translated transcript.

    Notes
    -----
    - The transcript is retrieved and translated using `YouTubeTranscriptApi`.
    - The translated text is formatted before being saved.
    - The output file name is generated randomly.
    - The file is saved in the "files/" directory.
    - If the directory does not exist, it is created automatically.
    """
    
    save_path = "files/"
    file_name = generate_random_string()

    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    transcript = transcript_list.find_transcript([source_language_code])
    translated_transcript = transcript.translate(target_language_code)

    translated_transcript = translated_transcript.fetch() #transforma em diciionario

    formatter = TextFormatter()
    text_formatted = formatter.format_transcript(translated_transcript)

    file_path = os.path.join(save_path, f"{file_name}.{doc_type}")
    save_file(file_path, text_formatted.replace('\n', ' '), doc_type)

    return file_path

