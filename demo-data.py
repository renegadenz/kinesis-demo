import boto3
import json

kinesis = boto3.client('kinesis')

stream_name = 'demo-kinesis-data-stream'
partition_key = 'test-data5'
message = 'Hello, Kinesis!'

response = kinesis.put_record(
    StreamName=stream_name,
    PartitionKey=partition_key,
    Data=json.dumps(message)
)

print(response)