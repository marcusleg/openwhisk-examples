#!/bin/bash
mkdir tmp-build
cp *.py tmp-build/

# install dependencies
pip3 install -r requirements.txt -t tmp-build/

# zip
cd tmp-build
zip -r -Z bzip2 -9 ../exec.zip ./*
cd ..

wsk action update machineLearning exec.zip --kind python:3 --memory 512 --timeout 300000

rm -rf tmp-build/ exec.zip
