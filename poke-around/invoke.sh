#!/bin/bash
while true; do
    echo -n "$ "
    read CMD
    OUTPUT=$(wsk action invoke pokeAround --param cmd "$CMD" --result | grep output | sed 's/"output": "\(.*\)"/\1/')
    echo $OUTPUT | sed -e 's/\\n/\n/g'
done
