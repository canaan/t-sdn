#!/bin/sh

import sys
import argparse
import pprint
import requests
import json
from copy import deepcopy

url = "http://nstar1:8091/NorthStar/API/v1/tenant/1/topology/1/te-lsps"
urlprefix = "http://nstar1:8091"
headers = {'content-type': 'application/json'}
authkey = ('admin', 'admin')
user = 'admin'
passwd = 'admin'

def error_exit (estr, code) :
    print estr
    sys.exit (code)

def northstar_api (suffix):
	r = requests.get (urlprefix + suffix, auth = authkey, verify = False)
	if r.status_code != 200 :
		error_exit ("Error %d: %s" % (r.status_code, r.text), r.status_code)
	return r.json ()

def northstar_api_no_data_put (suffix) :
	r = requests.put (urlprefix + suffix, auth = authkey, verify = False)
	if r.status_code != 200 :
		error_exit ("Error %d: %s" % (r.status_code, r.text), r.status_code)
	return r.text

def northstar_api_post (suffix, dictdata) :
	r = requests.post (urlprefix + suffix, data = json.dumps (dictdata), headers = headers, 
			auth = authkey, verify = False)
	if r.status_code != 200 :
		error_exit ("Error %d: %s" % (r.status_code, r.text), r.status_code)
	return r.text

def northstar_api_put (suffix, dictdata) :
	r = requests.put (urlprefix + suffix, data = json.dumps (dictdata), headers = headers,
			 auth = authkey, verify = False)
	if r.status_code != 200 :
		error_exit ("Error %d: %s" % (r.status_code, r.text), r.status_code)
	return r.text

def create_lsp(args):
	# create_lsp lsp_name From_ipadd To_ipadd Bandwidth
	try :
		(create_lsp, lsp_name, from_ipaddr, to_ipaddr, BW) = args
	except :
		error_exit ("invalid syntax %s" % ' '.join (args), -1)

	suffix = "/NorthStar/API/v1/tenant/1/topology/1/te-lsps" 
	data = {
		"name" : lsp_name,
		"from" : {
			"topoObjectType": "ipv4",
			"address" : from_ipaddr
		},
		"to" : {
			"topoObjectType": "ipv4",
			"address" : to_ipaddr
		},
		"plannedProperties": {
			"bandwidth": BW,
			"setupPriority": 7,
			"holdingPriority": 7
		}
	}
	res = northstar_api_post (suffix, data)
	print res

def explicit_lsp(args):
        # explicit_lsp lsp_name From_ipadd To_ipadd Bandwidth
        try :
                (explicit_lsp, lsp_name, from_ipaddr, to_ipaddr, via_ipaddr, BW) = args
        except :
                error_exit ("invalid syntax %s" % ' '.join (args), -1)

        suffix = "/NorthStar/API/v1/tenant/1/topology/1/te-lsps"
        data = {
		"name": lsp_name,
		"from": {
			"topoObjectType": "ipv4",
			"address": from_ipaddr
		},
		"to":   {
			"topoObjectType": "ipv4",
			"address": to_ipaddr
		},
		"plannedProperties": {
			"bandwidth": BW,
			"setupPriority": 7,
			"holdingPriority": 7,
			"ero" : [ {
				"topoObjectType": "ipv4",
				"address": via_ipaddr
	#			"loose": "true"
				}
			]
		}
	}
	print data

        res = northstar_api_post (suffix, data)
        print res


def usage ():
	print " create_lsp [LSP name] [From] [To] [Bandwidth] : create LSP without explicit route"
	print " explicit_lsp [LSP name] [From] [To] [via] [Bandwidth] : create LSP with explicit route"


def main():
	args = deepcopy (sys.argv)
	args.pop (0)

	if len (args) == 0 :
		usage ()
		error_exit ("invalid command", -1)

	commands = {
		"create_lsp" : create_lsp,
		"explicit_lsp": explicit_lsp,
	}

	if not commands.has_key (args[0]) :
		usage ()
		error_exit ("invalid command \"%s\"" % args[0], -1)

	commands[args[0]] (args)

	return


if __name__=='__main__':
	main()
