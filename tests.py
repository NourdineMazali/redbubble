"""
tests.py
Automated Tests for the Redbubble Coding Challenge
"""
import os
import unittest #For Automated Testing Purposes
from helper import Helper
from exceptions import InputNotValid #For the invalid schema Exception

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

if __name__ == '__main__':
    unittest.main()
