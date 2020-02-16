"""
Helper Class

"""
import json #For JSON Parsing
import os
from jsonschema.validators import validate
from exceptions import InputNotValid

class Helper:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    # ---------------------------------------------------------------------------- #
    # Helper Functions for Price Calculator
    # ---------------------------------------------------------------------------- #

    @staticmethod
    def load_schema(f, schema):
        """
        Validate if a file is a json and fits the schema

        :param f: path to file
        :param schema: name of the schema file
        :return:
        """
        if not os.path.exists(f):
            raise FileNotFoundError('File {path} not found'.format(path=f))
        try:
            with open(os.path.join(Helper.ROOT_DIR, 'schemas', schema), 'r') as schema_data:
                with open(f, 'r') as data:
                    content = json.loads(data.read())
                    schema = json.loads(schema_data.read())
                    validate(content, schema)
                    return content
        except Exception as e:
            raise InputNotValid('File: {path} is not a valid JSON format: {errors}'.format(
                path=f,
                errors=e.args
            ))