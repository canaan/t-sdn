#!/bin.sh

NS=nstar1
lspIndex=/home/y-kanaumi/northstar-rest_api-test/delete-lsp.json
#FILE=/home/y-kanaumi/northstar-rest_api-test/delete-lsp.json

curl -H "Content-type: application/json" -X POST http://$NS:8091/NorthStar/API/v1/tenant/1/topology/1/te-lsps/$lspIndex

