#!/bin/bash
export FUNCTION_NAME=fizzbuzz

set -e
for value in {1..20}
do
    wsk action invoke $FUNCTION_NAME -p n $value --result
done
