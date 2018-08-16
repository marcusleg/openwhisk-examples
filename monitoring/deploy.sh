#!/bin/bash
wskdeploy

read -p "Do you want to (re)configure the credentials for your SMTP server? [y/N]" -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    read -p "Hostname: " HOSTNAME
    read -p "Port (SSL): " PORT
    read -p "Email Address: " FROM
    read -p "Username: " USER
    read -p "Password: " -s PASSWORD
    echo ""
    wsk action update monitoring/sendmail -p smtp_host $HOSTNAME -p smtp_port $PORT -p smtp_from $FROM -p smtp_user $USER -p smtp_password $PASSWORD
fi
