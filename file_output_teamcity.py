#!/usr/bin/python

import json

print("listing of href for non-archived(active) jobs:")

with open('sample.json', mode='r') as f:
    json_data = json.load(f)

print("listing of href for non-archived(active) jobs:\n==============\n")

count = 0
for json_dict in json_data['project']:

    if not 'archived' in json_dict.keys():
         #print("value = ",json_dict['href'],json_dict['archived'])
         print(json_dict['id'], "href value =",json_dict['href'])
         count += 1


print("\n==============\n",count,"records")
