#!/bin/bash
wsk action delete updateInventory
wsk trigger delete restockDelivered
wsk trigger delete itemSold
wsk rule delete restockRule
wsk rule delete saleRule
