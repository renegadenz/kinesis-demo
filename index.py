import json
import boto3

kinesis = boto3.client('kinesis')
firehose = boto3.client('firehose')

stream_name = 'my-kinesis-data-stream'
delivery_stream_name = 'my-kinesis-firehose-delivery-stream'

def put_record(data):
    response = kinesis.put_record(
        StreamName=stream_name,
        PartitionKey='my-key',
        Data=json.dumps(data)
    )
    return response

def process_record(record):
    # TODO: process the record
    print(record)

def process_records(records):
    for record in records:
        process_record(record)

def consume_stream():
    shard_id = 'shardId-000000000000'
    response = kinesis.get_shard_iterator(
        StreamName=stream_name,
        ShardId=shard_id,
        ShardIteratorType='LATEST'
    )
    shard_iterator = response['ShardIterator']
    while True:
        response = kinesis.get_records(
            ShardIterator=shard_iterator,
            Limit=100
        )
        records = response['Records']
        if records:
            process_records(records)
            shard_iterator = response['NextShardIterator']

def deliver_stream():
    response = firehose.put_record(
        DeliveryStreamName=delivery_stream_name,
        Record={
            'Data': 'Hello, world!'
        }
    )
    return response

put_record({'message': 'Hello, Kinesis!'})
consume_stream()
deliver_stream()
