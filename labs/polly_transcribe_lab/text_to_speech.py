import boto3

polly = boto3.client('polly')
text = open("sample_text.txt").read()

response = polly.synthesize_speech(
    Text=text,
    OutputFormat='mp3',
    VoiceId='Joanna'
)

with open("output.mp3", 'wb') as file:
    file.write(response['AudioStream'].read())

print("Audio generated with Amazon Polly.")
