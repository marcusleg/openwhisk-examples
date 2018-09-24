#!/bin/bash
PRODUCT_ID=$(($RANDOM % 50))
RESTOCK=$(($RANDOM % 10 + 1))

echo "Firing itemRestocked trigger with product_id=$PRODUCT_ID and stock_change=$RESTOCK"
wsk trigger fire itemRestocked -p product_id $PRODUCT_ID -p stock_change $RESTOCK
sleep 1
wsk activation result --last

echo "Firing itemSold trigger with product_id=$PRODUCT_ID"
wsk trigger fire itemSold -p product_id $PRODUCT_ID
sleep 1
wsk activation result --last

