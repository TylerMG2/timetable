#!/bin/sh
export FLASK_APP=./backend/__init__.py
pipenv run flask --debug run -h 0.0.0.0