#!/bin/sh

NS=nstar1
HEADER=/home/y-kanaumi/northstar-rest_api-test/header
FILE1=/home/y-kanaumi/northstar-rest_api-test/explicit-lsp1-1.json
#FILE2=/home/y-kanaumi/northstar-rest_api-test/explicit-lsp1-2.json


curl -H $HEADER -X POST -d @$FILE1 http://$NS:8091/NorthStar/API/v1/tenant/1/topology/1/te-lsps 
#curl -H "Content-type: application/json" -X POST -d @$FILE2 http://$NS:8091/NorthStar/API/v1/tenant/1/topology/1/te-lsps

