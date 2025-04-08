import boto3

s3 = boto3.client('s3')
bucket_name = "your-s3-bucket-name"
object_key = "polly-audio/output.mp3"

s3.upload_file("output.mp3", bucket_name, object_key)
print(f"File uploaded to s3://{bucket_name}/{object_key}")
