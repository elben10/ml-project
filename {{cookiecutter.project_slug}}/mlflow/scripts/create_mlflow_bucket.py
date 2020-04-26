import os
from urllib.parse import urlparse

from minio import Minio

def create_bucket(bucket_name):
    url = urlparse(os.environ["MLFLOW_S3_ENDPOINT_URL"])
    minioClient = Minio(
        url.netloc,
        access_key=os.environ["AWS_ACCESS_KEY_ID"],
        secret_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        secure=False,
    )
    minioClient.make_bucket(bucket_name)

if __name__ == "__main__":
    create_bucket("mlflow")