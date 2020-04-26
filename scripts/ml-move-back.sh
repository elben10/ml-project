#! /usr/bin/env bash

# Run this script from outside the project, to integrate a dev-fsfp project with changes and review modifications

# Exit in case of error
set -e

if [ ! -d ./dev-ml ] ; then
    echo "Run this script from outside the project, to integrate a sibling dev-fsfp project with changes and review modifications"
    exit 1
fi

rsync -a --exclude=node_modules --exclude=README.md ./dev-ml/* ./ml-project/\{\{cookiecutter.project_slug\}\}/