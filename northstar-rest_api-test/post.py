#!/bin/sh

import sys
import argparse
import pprint
import requests
import json

url = "http://nstar1:8091/NorthStar/API/v1/tenant/1/topology/1/te-lsps"
headers = {'content-type': 'application/json'}
token = "+c2BEU0I0ydaVBFTpijNRWp1YQsw/pm+XpKa4q40zW4="
user = 'admin'
passwd = 'admin'

def no_explicit():
	with open('/home/y-kanaumi/northstar-rest_api-test/rest-lsp1-2.json') as post_data:
		data = json.dumps(json.load(post_data))
	response = requests.post(url, data=data, headers=headers)
	pprint.pprint(response.json())

def explicit():
        with open('/home/y-kanaumi/northstar-rest_api-test/explicit-lsp1-2.json') as post_data:
                data = json.dumps(json.load(post_data))
	response = requests.post(url, data=data, headers=headers, auth=(user, passwd))
	pprint.pprint(response.json())

def create_lsp():
        with open('/home/y-kanaumi/northstar-rest_api-test/explicit-lsp1-2.json') as post_data:
                data = json.dumps(json.load(post_data))
        response = requests.post(url, data=data, headers=headers, auth=(user, passwd))
        pprint.pprint(response.json())


if __name__=='__main__':
#	create_lsp()
#	no_explicit()
	explicit()
	parser = argparse.ArgumentParser()
	args = parser.parse_args()
