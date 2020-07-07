#!/bin/bash

docker build -t pp .
docker run --rm -v $(pwd):/app pp python /app/output_teamcity_json.py
