#!/bin/python

import urllib
import urllib2
import json
import requests

url = "http://nstar1:8091/NorthStar/API/v1/tenant/1/topology/1/te-lsps"
token = "+c2BEU0I0ydaVBFTpijNRWp1YQsw/pm+XpKa4q40zW4="

files = {'file': open('/home/y-kanaumi/northstar-rest_api-test/rest-lsp1-2.json', 'rb')}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, files=json.load(files), headers=headers)

print response.text
