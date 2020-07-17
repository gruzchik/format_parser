#!/bin/bash

cat <<EOF >> settings.py
TC_USERNAME=$user_variable
TC_PASSWORD=$pass_variable
TC_URL=$teamcity_url
EOF

docker build -t pp .
docker run --rm -v $(pwd):/app pp python /app/output_teamcity_json.py
