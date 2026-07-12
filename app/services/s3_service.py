import uuid

import boto3
from fastapi import UploadFile

from app.core.aws_secrets import get_secret


secret = get_secret("book-store-secrets")


class S3Service:

    def __init__(self):

        self.bucket_name = secret["S3_BUCKET_NAME"]

        self.client = boto3.client(
            "s3",
            region_name="ap-south-1",
        )

    def upload_image(
        self,
        file: UploadFile,
    ) -> str:

        extension = file.filename.split(".")[-1]

        file_name = f"books/{uuid.uuid4()}.{extension}"

        self.client.upload_fileobj(
            file.file,
            self.bucket_name,
            file_name,
            ExtraArgs={
                "ContentType": file.content_type,
            },
        )

        return (
            f"https://{self.bucket_name}.s3.ap-south-1.amazonaws.com/{file_name}"
        )