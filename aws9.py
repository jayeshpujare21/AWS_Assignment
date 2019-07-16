import boto3
import time
import logging

logging.basicConfig(format='{asctime}.{msecs:03.0f} {filename}:{lineno} {levelname} {message}',
                    level=logging.DEBUG, style='{', datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log9.txt', filemode='a')



def create_games_table(dynamodb_client):
    try:
        dt_response = dynamodb_client.describe_table(TableName='jayGames')
        logging.debug(dt_response)
        print("Table already exists")  # Skip Table creation if it already exists.
        logging.info("Table already exists")
    except dynamodb_client.exceptions.ResourceNotFoundException:
        dynamodb_client.create_table(
            TableName='jayGames',
            KeySchema=[
                {
                    'AttributeName': 'gid',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'gname',
                    'KeyType': 'RANGE'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'gid',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'gname',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'rating',
                    'AttributeType': 'N'
                },
            ],
            LocalSecondaryIndexes=[  # Used for query in a10.py
                {
                    'IndexName': 'gid_rating_index',
                    'KeySchema': [
                        {
                            'AttributeName': 'gid',
                            'KeyType': 'HASH'
                        },
                        {
                            'AttributeName': 'rating',
                            'KeyType': 'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'KEYS_ONLY'
                    },
                },
            ],
            BillingMode='PROVISIONED',
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            },

        )
        while True:  # Loop to pause till table is active.
            dt_response = dynamodb_client.describe_table(TableName='Games')
            logging.debug(dt_response)
            if dt_response['Table']['TableStatus'] != 'ACTIVE':
                print("Waiting for table creation...")
                time.sleep(5)
            else:
                break
        print("Successfully created table")

def add_items(dynamodb_client):
    response1 = dynamodb_client.put_item(
        TableName='jayGames',
        Item={
            'gid': {
                'N': "1",
            },
            'gname': {
                'S': "Cricket",
            },
            'publisher': {
                'S': "ENG",
            },
            'rating': {
                'N': "5",
            },
            'release_date': {
                'S': "2019/01/01",
            },
        }
    )
    logging.debug(response1)
    response2 = dynamodb_client.put_item(
        TableName='jayGames',
        Item={
            'gid': {
                'N': "1",
            },
            'gname': {
                'S': "Hockey",
            },
            'publisher': {
                'S': "pa",
            },
            'rating': {
                'N': "2",
            },
            'release_date': {
                'S': "2019/01/02",
            },
        }
    )
    logging.debug(response2)
    response3 = dynamodb_client.put_item(
        TableName='jayGames',
        Item={
            'gid': {
                'N': "2",
            },
            'gname': {
                'S': "Tennis",
            },
            'publisher': {
                'S': "pb",
            },
            'rating': {
                'N': "5",
            },
            'release_date': {
                'S': "2019/01/03",
            },
        }
    )
    logging.debug(response3)
    print("Added items to table")
    logging.info("Added items to table")


if __name__ == '__main__':
    dynamodb_client = boto3.client('dynamodb', region_name='us-east-1')
    create_games_table(dynamodb_client)
    add_items(dynamodb_client)
