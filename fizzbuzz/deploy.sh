#!/bin/bash
wsk action update fizzbuzz main.py --kind python:3 --memory 128 --timeout 5000
