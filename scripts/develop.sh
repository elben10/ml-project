#! /usr/bin/env bash

# Exit in case of error
set -e

# Remove legacy project
rm -fr ./testing-project

# Create testing project
cookiecutter . --no-input project_name=testing-project

# Go into project
cd testing-project

# Remove containers
docker-compose rm -f

# Begin docker compose
docker-compose up --build

# Remove containers
docker-compose rm -f

# Move to root project
cd ..