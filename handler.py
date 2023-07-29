import json
import boto3

s3_client = boto3.client("s3")
S3_BUCKET = 'sample-lambda-read-4455'

def lambda_handler(event, context):
    object_key = "readme.txt"  # replace object key
    file_content = s3_client.get_object(
        Bucket=S3_BUCKET, Key=object_key)["Body"].read()
    print(file_content)
    # TODO implement
    return {
        'statusCode': 200,
        'body': file_content
    }