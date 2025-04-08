import boto3
import time
import json

transcribe = boto3.client('transcribe')
job_name = "PollyTranscriptionJob"

while True:
    result = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    status = result['TranscriptionJob']['TranscriptionJobStatus']
    
    if status in ['COMPLETED', 'FAILED']:
        break
    print("Waiting for transcription to complete...")
    time.sleep(5)

if status == 'COMPLETED':
    transcript_url = result['TranscriptionJob']['Transcript']['TranscriptFileUri']
    print(f"Transcript ready at: {transcript_url}")
else:
    print("Transcription failed.")
