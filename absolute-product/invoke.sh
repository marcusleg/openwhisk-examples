#!/bin/bash
echo "Example invocation #1:"
wsk action invoke absoluteProduct/main --result --param a 12.34 --param b 42

echo "Example invocation #1:"
wsk action invoke absoluteProduct/main --result --param a 14.2 --param b -2.3
