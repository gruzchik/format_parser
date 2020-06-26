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



#formatted_json = json.dumps(json.loads(get_data.content), indent=4)
formatted_json = json.loads(get_data.content)

print("listing of href for non-archived(active) jobs:\n==============\n")

count = 0
for json_dict in formatted_json['project']:

    if not 'archived' in json_dict.keys():
         print(json_dict['id'], "value = ",json_dict['href'])

         project_id = json_dict['href'].split('id:')[1]
         print ("id = ", project_id)

         activebranch_url = "http://localhost:8080/app/rest/projects/"+project_id+"/branches?locator=policy:ACTIVE_VCS_BRANCHES"
         print(activebranch_url)

         count += 1


print("\n==============\n",count,"records")
