# Inventory Example
This example is meant to showcase the following things while being as concise as possible:
* actions that require external libraries
* triggers and rules
* default parameters for triggers

In order to keep this example as short as possible there is no input validation or sanity checking.


## Requirements
* Apache OpenWhisk
* MongoDB


## How to run this example. 
1. Install and configure **wsk** the OpenWhisk client.
2. Set 'mongo_url' in '__main__.py' to the URL of your MongoDB cluster.
3. Run `./deploy.sh` to deploy the action, triggers and rules.
4. Run `./fire_triggers.sh` to fire both triggers with randomly generated values.
