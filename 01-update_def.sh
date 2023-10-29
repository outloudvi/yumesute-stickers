#!/bin/bash
wget https://raw.githubusercontent.com/sir-ius/sirius-master-diff/master/StampMaster.json -O StampMaster.json
jq '.[] | ((.Id | tostring) + "," + .Name + ",")' -r StampMaster.json >def.full.txt
