#!/bin/bash

source settings.py

GET_DATA=$(curl -u $TC_USERNAME:$TC_PASSWORD -s -H 'Accept: application/json' http://localhost:8080/app/rest/projects)

echo $GET_DATA | python -m json.tool
