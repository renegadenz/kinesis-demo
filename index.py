import json
import base64 
import boto3

kinesis = boto3.client('kinesis')
firehose = boto3.client('firehose')

stream_name = 'demo-kinesis-data-stream'
delivery_stream_name = 'demo-kinesis-firehose-delivery-stream'

def handler(event, context):
    # Process the incoming Kinesis Data Stream records
    for record in event['Records']:
        # Decode the base64 encoded data
        payload = base64.b64decode(record["kinesis"]["data"])
        print(f"Decoded payload: {payload}")  # Add this line to print the payload
        # Deserialize the JSON object
        data = json.loads(payload)
        # Process the record
        process_record(data)

def process_record(record):
    # TODO: process the record
    print(record)

def process_records(records):
    for record in records:
        process_record(record)
