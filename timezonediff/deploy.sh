wsk package update timezonediff

# deploy difference function
GOOS=linux GOARCH=amd64 go build -o exec
zip exec.zip exec
wsk action update timezonediff/difference --native exec.zip
rm exec exec.zip

# deploy offset function
wsk action update timezonediff/offset offset.js

# deploy main function
wsk action update timezonediff/main main.js
