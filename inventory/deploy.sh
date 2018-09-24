#!/bin/bash
mkdir tmp-build
cp *.py tmp-build/

# install dependencies
pip3 install dnspython pymongo -t tmp-build/

# zip
cd tmp-build
zip -r ../exec.zip ./*
cd ..

# create action
wsk action create updateInventory exec.zip --kind python:3

# delete artifacts
rm -rf tmp-build/ exec.zip

# create/update triggers and rules
wsk trigger create itemRestocked -p stock_change 1 
wsk trigger create itemSold -p stock_change -1
wsk rule create restockRule itemRestocked updateInventory
wsk rule create saleRule itemSold updateInventory
