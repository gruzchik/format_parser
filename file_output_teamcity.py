#!/usr/bin/python

import json


with open('sample.json', mode='r') as f:
    json_data = json.load(f)

print("listing of href for non-archived(active) jobs:\n==============\n")

count = 0
for json_dict in json_data['project']:

    if not 'archived' in json_dict.keys():
         #print("value = ",json_dict['href'],json_dict['archived'])
         print(json_dict['id'], "href value =",json_dict['href'])

         project_id = json_dict['href'].split('id:')[1]
         print ("id = ", project_id)

         activebranch_url = "http://localhost:8080/app/rest/projects/"+project_id+"/branches?locator=policy:ACTIVE_VCS_BRANCHES"
         print(activebranch_url)

         count += 1


print("\n==============\n",count,"records")
