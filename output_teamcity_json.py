#!/usr/bin/python
import urllib.request
import json
import settings
from settings import *
from requests import get

headers = {
    'Accept': 'application/json',
}

get_data = get(TC_URL+"/app/rest/projects", auth=(TC_USERNAME, TC_PASSWORD), headers=headers)

#formatted_json = json.dumps(json.loads(get_data.content), indent=4)
formatted_json = json.loads(get_data.content)

print("listing of href for non-archived(active) jobs:\n==============\n")

COUNT = 0
for json_dict in formatted_json['project']:
    if json_dict['id'] != '_Root':
        if not 'archived' in json_dict.keys():
            # output href
            #print(json_dict['id'], "value = ",json_dict['href'])

            project_id = json_dict['href'].split('id:')[1]
            #print ("id = ", project_id)

            activebranch_url = TC_URL+"/app/rest/projects/"+project_id+"/branches?locator=policy:ACTIVE_VCS_BRANCHES"
            get_activebranch = get(activebranch_url, auth=(TC_USERNAME, TC_PASSWORD), headers=headers)

            formatted_abranches = json.loads(get_activebranch.content)
            if formatted_abranches['COUNT'] != 0:
                # output json
                # print('result = ',formatted_abranches)
                print(activebranch_url)
                for abranches_dict in formatted_abranches['branch']:
                    abranch_output = "Project = %s; Active branch = %s" % (project_id, abranches_dict['name'])
                    print(abranch_output)
                print("\n")
            else:
                print("\n")
            COUNT += 1

print("\n==============\n",COUNT,"records")
