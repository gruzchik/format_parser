#!/bin/bash

source settings.py

while getopts t: opts; do
   case ${opts} in
	    t) TYPE_OUTPUT=${OPTARG} ;;
   esac
done

# choose type of output

if [[ $TYPE_OUTPUT == 'json' ]]; then
   OUTPUT_PARAMETER="-H 'Accept: application/json'"
   GET_DATA=$(curl -u $TC_USERNAME:$TC_PASSWORD -s -H 'Accept: application/json' http://localhost:8080/app/rest/projects)
   echo $GET_DATA | python -m json.tool

elif [[ $TYPE_OUTPUT == 'xml' ]] || [[ -z $TYPE_OUTPUT ]]; then
  GET_DATA=$(curl -u $TC_USERNAME:$TC_PASSWORD -s http://localhost:8080/app/rest/projects)
  echo $GET_DATA | python -c 'import sys;import xml.dom.minidom;s=sys.stdin.read();print(xml.dom.minidom.parseString(s).toprettyxml())'

else
  GET_DATA=$(curl -u $TC_USERNAME:$TC_PASSWORD -s http://localhost:8080/app/rest/projects)
  echo $GET_DATA | python -c 'import sys;import xml.dom.minidom;s=sys.stdin.read();print(xml.dom.minidom.parseString(s).toprettyxml())'
fi
