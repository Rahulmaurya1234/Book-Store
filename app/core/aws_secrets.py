import json

import boto3


def get_secret(secret_name: str):

    client = boto3.client(
        "secretsmanager",
        region_name="ap-south-1",
    )

    response = client.get_secret_value(
        SecretId=secret_name,
    )

    return json.loads(
        response["SecretString"]
    )