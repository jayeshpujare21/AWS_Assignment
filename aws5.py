#Lambda function to copy object from one s3 to another
import urllib
import boto3
import ast
import json
print('Loading function')

s3 = boto3.client('s3')
    
def lambda_handler(event, context):
    target_bucket = 'jayeshcopybucket'
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    copy_source = {'Bucket':source_bucket, 'Key':key}
    s3.copy_object(Bucket=target_bucket, Key=key, CopySource=copy_source)
