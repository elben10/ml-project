#! /usr/bin/env bash

# Exit in case of error
set -e

python /scripts/test_pre_start.py

airflow initdb

airflow webserver