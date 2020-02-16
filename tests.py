"""
tests.py
Automated Tests for the Redbubble Coding Challenge
"""
import os
import unittest #For Automated Testing Purposes
from helper import Helper
from exceptions import InputNotValid #For the invalid schema Exception
from redbubble import Cart, PriceFinder, Calculator #Price Calculator Class - Find Price

# ---------------------------------------------------------------------------- #
# Initialization of Testing Variables - Easily Extendible and Dynamic!
# ---------------------------------------------------------------------------- #
root = os.path.join(Helper.ROOT_DIR, 'test_files', 'carts')
list_of_cart_jsons = [
    os.path.join(root, 'cart-4560.json'), \
    os.path.join(root, 'cart-9363.json'), \
    os.path.join(root, 'cart-9500.json'), \
    os.path.join(root, 'cart-11356.json'), \
    os.path.join(root, 'cart-0.json'), \
    os.path.join(root, 'cart-no-options-one-item.json'), \
    os.path.join(root, 'cart-repeat-item-quantity.json')]

list_of_price_jsons = [os.path.join(Helper.ROOT_DIR, 'test_files','base_prices','base-prices.json')]

list_of_checkout_prices = [4560, 9363, 9500, 11356, 0, 19500, 9120]

list_of_cart_item_count = [1, 2, 2, 1, 0, 1, 2]

list_of_price_item_count = [10]

list_of_mark_up_prices = [4560, 9120, 243, 4560, 4940, 11356 ,19500, 4560, 4560]

class TestFilesValidation(unittest.TestCase):
    """Tests for `cli` command line module."""

    def test_file_not_exists(self):
        with self.assertRaises(FileNotFoundError):
            Helper.load_schema(
                f='/path/not/exists',
                schema='base-prices.schema.json'
            )
        with self.assertRaises(FileNotFoundError):
            Helper.load_schema(
                f='cart-4560.json',
                schema='/path/not/exists'
            )

    def test_invalid_file(self):
        with self.assertRaises(InputNotValid):
            Helper.load_schema(
                f=os.path.join(Helper.ROOT_DIR, 'test_files', 'test_carts' , 'cart-4560.json'),
                schema=os.path.join(Helper.ROOT_DIR, 'test_files', 'test_invalid_schemas', 'base-prices-invalid-format.json')
            )
        with self.assertRaises(InputNotValid):
            Helper.load_schema(
                f=os.path.join(Helper.ROOT_DIR, 'test_files', 'test_carts' , 'cart-4560.json'),
                schema=os.path.join(Helper.ROOT_DIR, 'test_files', 'test_invalid_schemas', 'base-prices-invalid-json.json')
            )


class TestPriceCalculator(unittest.TestCase):

    def test_cart_prices_json(self):
        print()
        print("Following Tests tested with Base Price File: " + \
        list_of_price_jsons[0] + ":")
        print()
        for i in range(0, len(list_of_cart_jsons)):
            print("Testing Cart JSON File: " + list_of_cart_jsons[i] + \
            " with Expected Cart Value of " + str(list_of_checkout_prices[i]))

            #Testing Base - cli.py
            cart_json = Helper.load_schema(list_of_cart_jsons[i], 'cart.schema.json')
            price_json = Helper.load_schema(list_of_price_jsons[0], 'base-prices.schema.json')
            rb_cart = Cart(cart_json)
            price_finder = PriceFinder(price_json)
            price_calculator = Calculator(rb_cart, price_finder)
            actual_cart_value = price_calculator.get_total()
            print("Actual Cart Value: " + \
                  str(price_calculator.get_total()), end ='')

            self.assertEqual(actual_cart_value, list_of_checkout_prices[i])
            print(" - PASS")
            print()
        print("-----------------------------------------------------------------------")

    def test_cart_item_count(self):
        for i in range(0, len(list_of_cart_jsons)):
            print("Testing Cart JSON File: " + list_of_cart_jsons[i] + \
            " with Expected Cart Item Amount of " + \
            str(list_of_cart_item_count[i]))

            #Testing Cart Class
            cart_json = Helper.load_schema(list_of_cart_jsons[i], 'cart.schema.json')
            rb_cart = Cart(cart_json)
            actual_cart_item_amount = len(rb_cart.get_product_items())
            print("Actual Cart Item Amount: " + str(actual_cart_item_amount), \
            end = "")

            self.assertEqual(actual_cart_item_amount, \
            list_of_cart_item_count[i])
            print(" - PASS")

    def test_mark_up_prices(self):
        print()
        mark_up_prices_index = 0
        for i in range(0, len(list_of_cart_jsons)):
            print("Testing Cart JSON File: " + list_of_cart_jsons[i])
            #Testing Cart and PriceFinder Class
            cart_json = Helper.load_schema(list_of_cart_jsons[i], 'cart.schema.json')
            rb_cart = Cart(cart_json)
            price_json = Helper.load_schema(list_of_price_jsons[0], 'base-prices.schema.json')
            price_finder = PriceFinder(price_json)

            calculator = Calculator(rb_cart, price_finder)

            list_of_cart_items = rb_cart.get_product_items()

            for product in list_of_cart_items:
                self.assertEqual(price_finder.get_price_point(product),\
            list_of_mark_up_prices[mark_up_prices_index])
                mark_up_prices_index = mark_up_prices_index + 1
                print(" - PASS")
                print()
            print(list_of_cart_jsons[i] + " = PASS")

if __name__ == '__main__':
    unittest.main()
