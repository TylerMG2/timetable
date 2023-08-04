#!/bin/sh
export FLASK_APP=./app
pipenv run flask --debug run -h 0.0.0.0