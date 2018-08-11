#!/bin/bash
zip exec.zip index.php header.html footer.html
wskdeploy
rm exec.zip

echo -n "The URL of your website is: "
wsk action get dynamicWebsite/index --url | sed -n 2p
