import logging
import boto3
from botocore.exceptions import ClientError
from app.core.config import config


s3_client = boto3.client('s3')


def upload_file(
    file_name,# file want upload
    object_name# name file
):
    try:
        _ = s3_client.upload_fileobj(
            file_name.file,
            config.buckets,
            object_name
        )
    except ClientError as e:
        raise logging.error(e)
    return True


def create_presigned_url(
    object_name,
    expiration=3600
):
    try:
        response = s3_client.\
            generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': config.buckets,
                    'Key': object_name
                },
                ExpiresIn=expiration
            )
    except ClientError as e:
        raise logging.error(e)

    return response


def dowload_file():
    s3 = boto3.resource('s3')

    my_bucket = s3.Bucket('bucket_name')

    for file in my_bucket.objects.all():
        print(file.key)
    return 1


def delete_file(
    obj: str
):
    try:
        response = s3_client.delete_object(
            Bucket=config.buckets,
            Key=obj,
        )
    except ClientError as e:
        raise logging.error(e)

    return response


def get_file_name(file_name: str, id_question: str):
    list_item = file_name.split('.')
    return f'{id_question}.{list_item[-1]}'
