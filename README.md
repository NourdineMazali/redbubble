# Redbubble Coding Challenge
Redbubble Price Calculator - Coding Test

## Purpose
* http://take-home-test.herokuapp.com/new-product-engineer
* Create a Price Calculator Command Line Application to output the Total Price of the Redbubble Shopping Cart (in Cents)

## Technologies Used
* Docker (optional)
* Python 3.7

## Dependencies Needed
* Python3 (Python2 is compatible as well)
* argparse library
* jsonschema library 

##Getting Started

### Option 1 : Use Local python

1.Download and install the lastest version of Python 3.7

2.Clone the project

3.Install library requirements:

```
pip install -r requirements.txt
```

### Option 2 : Run using Docker
1.Install Docker

2.Build and access the Python Container 
```
docker build -t redbubble:v1 .
docker run -it -v C:/redbubble:/app redbubble:v1 bash
```

### Usage
To get the Total Price of the Redbubble Shopping Cart (in Cents), run: 
```
python cli.py -c /PATH_TO_CART_JSON -p /PATH_TO_BASE_PRICE_JSON
```
Example:
```
python3 cli.py -c test_files/test_carts/cart-9363.json -p test_files/test_base_prices/base-prices.json
```