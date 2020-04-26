#! /usr/bin/env bash

# Exit in case of error
set -e

python /scripts/test_pre_start.py
python /scripts/create_mlflow_bucket.py
mlflow server --host 0.0.0.0 --default-artifact-root s3://mlflow/ --backend-store-uri postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_SERVER}/mlflow