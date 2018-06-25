export FUNCTION_NAME=fibonacci

wsk action get $FUNCTION_NAME &>/dev/null
if [ $? -eq 0 ]; then
    wsk action update $FUNCTION_NAME main.py
else
    wsk action create $FUNCTION_NAME main.py --kind python:3 --memory 256
fi
