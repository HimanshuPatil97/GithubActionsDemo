import boto3
import os

bucket_name = os.environ.get("S3_BUCKET")

s3 = boto3.client('s3')

s3.upload_file('index.html', 'mygithub-automation', 'index.html')
