#!/usr/bin/python
import urllib.request
import json
import settings
from settings import *


headers = {
    'Accept': 'application/json',
}

from requests import get
get_data = get('http://localhost:8080/app/rest/projects', auth=(TC_USERNAME, TC_PASSWORD), headers=headers)


#print(url.content)

formatted_json = json.dumps(json.loads(get_data.content), indent=4)

print(formatted_json)
