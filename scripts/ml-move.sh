#! /usr/bin/env bash

# Exit in case of error
set -e

if [ ! -d ./ml-project ] ; then
    echo "Run this script from outside the project, to generate a sibling dev-fsfp project with independent git"
    exit 1
fi

rm -rf ./dev-ml

cookiecutter --no-input -f ./ml-project project_name="Dev ml"