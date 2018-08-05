# compile difference action
GOOS=linux GOARCH=amd64 go build -o exec
zip difference.zip exec

# deploy package
wskdeploy 

# remove compilation artefacts
rm exec difference.zip
