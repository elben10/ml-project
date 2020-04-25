#! /usr/bin/env bash

# Exit in case of error
set -e

# Remove legacy project
rm -fr ./testing-project

# Create testing project
cookiecutter . --no-input project_name=testing-project