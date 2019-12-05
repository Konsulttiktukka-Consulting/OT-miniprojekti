#!/bin/bash

FILE=/$PWD/venv/bin/activate
if test -f "$FILE"; then
   echo "$FILE found"
else
   echo "$FILE does not exist, creating new"
   python3 -m venv venv
fi

source /venv/bin/activate
venv/bin/pip install -r requirements.txt
export FLASK_APP=application
flask init-db
flask run

