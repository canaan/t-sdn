#!/bin/sh

import pprint
import requests

url = "http://nstar1:8091/NorthStar/API/v1/tenant/1/topology/1/te-lsps"

def main():
	response = requests.get(url)
	pprint.pprint(response.json())

if __name__=='__main__':
	main()
