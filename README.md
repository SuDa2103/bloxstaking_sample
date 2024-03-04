# Bloxstaking Sample

A simple python script to find the performance of all validators belonging to one operator. 


## Pre-Requisites

Make sure these are installed on your machine before runing the script. You can test whether they are installed by running the respective commands on your machine. 

1. python3

```
python3 --version
```

2. pip3

```
pip3 --version
```

For this script, we will only need access to the requests library so lets make sure this is installed. 

```
pip3 install requests
```


## Getting Started
Clone this repo onto your local machine so you have access to all the files and can change them as you need.

```
git clone https://github.com/SuDa2103/bloxstaking_sample.git
```
This should create you a folder named `blokstaking_sample` that you will use for the rest of this README.

Make sure you substitute `<YOUR_KEY>` in the `validators.py` script with your rated.network API key.

At this point, you should be ready to run the script using the following command.

```
  python3 validators.py <network> <operator_id>
```

Make sure to substitute `network` with one of these values: `holesky` or `mainnet`, and `operator_id` argument must be an integer.
