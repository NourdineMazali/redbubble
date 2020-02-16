""" cli.py
http://take-home-test.herokuapp.com/new-product-engineer
Price Calculator Command-Line Program - Outputs the Total Price in the User's
Shopping Cart in Cents.

USAGE: python3 cli -c /PATH_TO_CART_JSON -p /PATH_TO_BASE_PRICE_JSON

"""
# ---------------------------------------------------------------------------- #
# Import Statements for the Necessary Packages / Modules
# ---------------------------------------------------------------------------- #
import argparse #For Argument Parsing
from helper import Helper # Helper class


def main():
    """
    main Function for Calculating the Price
    in the Redbubble Shopping Cart in   Cents.

    Args:
        self (none): None.
    Returns:
        (void): No return value. Just prints the Total Price in the Cart
        in Cents
    """
    # ------------------------------------------------------------------------ #
    # Constructs Argument Parser for Parsing Arguments
    # ------------------------------------------------------------------------ #
    argument_parser = argparse.ArgumentParser(description='Price Calculator')
    argument_parser.add_argument("-c", "--cart", required=True, help="PATH TO CART JSON")
    argument_parser.add_argument("-p", "--price", required=True, help="PATH TO BASE PRICE JSON")

    arguments = vars(argument_parser.parse_args())

    # ------------------------------------------------------------------------ #
    # Validate and Load JSON Paths for Cart, Base Prices
    # ------------------------------------------------------------------------ #
    path_to_cart = arguments['cart']
    path_to_price = arguments['price']

    cart_json = Helper.load_schema(path_to_cart, 'cart.schema.json')
    price_json = Helper.load_schema(path_to_price, 'base-prices.schema.json')