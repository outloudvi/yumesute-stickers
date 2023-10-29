#!/bin/bash
set -eu

wget https://raw.githubusercontent.com/sir-ius/sirius-master-diff/master/assets/__asset_version -O asset_version
ASSET_VERSION=$(cat asset_version)

for i in $(cat def2.txt | cut --delimiter=',' --fields=1); do
    wget --user-agent="FaithInExpression-Sticker-Bot/1.0.0" "https://assets.wds-stellarium.com/production/2d-assets/Android/${ASSET_VERSION}/stamps_assets_stamp/${i}.bundle"
done
