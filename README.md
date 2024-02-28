# Bloxstaking_sample

A simple python script to find the performance of all validators belonging to one operator. 


## Getting Started
Clone this repo onto your local machine so you have access to all the files and can change them as you need.

git clone https://github.com/vegaprotocol/sample-api-scripts.git
This should create you a folder named sample-api-scripts that you will use for the rest of this README.


source vega-config
You can define, copy or edit your own configurations. Out of the box, the vega-config file is included for ease and defaults to the Fairground testnet with hosted wallet configuration. Node: Don't forget to source your configs after making any changes.

Navigate to the API transport you would like to explore, for example:

cd ./rest
Follow the sub-folder README.md information on how to run the samples.

For most scripts, you will have to run the login script before running the script in question. It's also important to note that you should have a desktop or CLI wallet connection open as you run this script, otherwise the connection will be refused.

  python3 login.py
