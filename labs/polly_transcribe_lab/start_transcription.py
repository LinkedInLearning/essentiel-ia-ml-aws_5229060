import boto3
import time
from difflib import SequenceMatcher

transcribe = boto3.client('transcribe')
job_name = "PollyTranscriptionJob"
file_uri = "s3://your-s3-bucket-name/polly-audio/output.mp3"


def similar(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': file_uri},
    MediaFormat='mp3',
    LanguageCode='en-US'
)

print("Transcription job started.")

similarity = similar(original_text, transcribed_text)
print(f"Text similarity: {similarity * 100:.2f}%")
