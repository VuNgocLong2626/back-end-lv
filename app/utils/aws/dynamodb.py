import boto3
from app.core.config import config

resource = boto3.resource(
    'dynamodb',
    region_name=config.region_name
)

client = boto3.client(
    'dynamodb',
    region_name=config.region_name
)

table = resource.Table(config.table)
