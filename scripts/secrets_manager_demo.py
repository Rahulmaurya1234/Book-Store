import boto3
import json

client = boto3.client(
    "secretsmanager",
    region_name="ap-south-1"
)

response = client.get_secret_value(
    SecretId="book-store-secrets"
)

secret = json.loads(response["SecretString"])

print(secret)
print(secret["DB_USER"])
print(secret["DB_PASSWORD"])
