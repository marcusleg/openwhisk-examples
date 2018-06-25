export FUNCTION_NAME=fizzbuzz

bluemix wsk action get $FUNCTION_NAME &>/dev/null
if [ $? -eq 0 ]; then
    bluemix wsk action update $FUNCTION_NAME main.py    
else
    bluemix wsk action create $FUNCTION_NAME main.py --kind python:3 --memory 128 --timeout 5000 
fi
