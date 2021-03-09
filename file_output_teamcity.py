#!/usr/bin/python

import json

with open('sample.json', mode='r') as f:
    json_data = json.load(f)

print("listing of href for non-archived(active) jobs:\n==============\n")

count = 0
connection_status = 0

for json_dict in json_data['project']:

    if not 'archived' in json_dict.keys():
        #print("value = ",json_dict['href'],json_dict['archived'])
        print(json_dict['id'], "href value =",json_dict['href'])

        project_id = json_dict['href'].split('id:')[1]
        print ("id = ", project_id)

        activebranch_url = "http://localhost:8080/app/rest/projects/"+project_id+"/branches?locator=policy:ACTIVE_VCS_BRANCHES"
        print(activebranch_url)
       
        if connection_status == 1:
            get_activebranch = get(activebranch_url, auth=(TC_USERNAME, TC_PASSWORD), headers=headers)

            formatted_abranches = json.loads(get_activebranch.content)
            if formatted_abranches['count'] != 0:
                # output json
                # print('result = ',formatted_abranches)
                for abranches_dict in formatted_abranches['branch']:
                    print("project = ",project_id,"active branch = ",abranches_dict['name'])
                print("\n")
            else:
                print("\n")

        count += 1

print("\n==============\n",count,"records")
