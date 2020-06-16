#!/usr/bin/python
import urllib.request
import sys
import xml.dom.minidom

import settings
from settings import *


from requests import get
get_data = get('http://localhost:8080/app/rest/projects', auth=(TC_USERNAME, TC_PASSWORD))

#print(get_data.content)

print(xml.dom.minidom.parseString(get_data.content).toprettyxml())


