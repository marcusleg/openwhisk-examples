# Monitoring and Alerting for HTTP and DNS
Periodically checks the availability of web servers and verify the correctness of DNS entries.


## How to deploy
Run `./deploy.sh`. On the first deployment you'll need to configure credentials for the email address that will send out alerts.


## Test actions individually
You may invoke individual actions of this package with commands such as:
```
wsk action invoke monitoring/sendmail --result -p to me@example.com -p subject Test -p body "Hello World"
wsk action invoke monitoring/checkHTTP --result -p url http://www.google.com -p expected_status_code 301
wsk action invoke monitoring/checkHTTP --result -p url https://www.google.com -p expected_status_code 200
```
