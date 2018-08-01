#!/bin/bash
wsk package update conductors-example
wsk action update conductors-example/triple triple.js
wsk action update conductors-example/increment increment.js
wsk action update conductors-example/tripleAndIncrement tripleAndIncrement.js -a conductor true
