import json
"""
    Domain module defines the objects related with the business model.
    PriceFinder, Cart, CartItem, Calculator.
"""


class CartItem:
    """
    CartItem Class - Represents a CartItem in the Redbubble Shopping
    Cart.

    Attributes:
        _product_type (String): The Type of the CartItem Being Purchased.
        _options (Key-value pairs of strings.): Options that the CartItem
        Falls Under.
        _artist_markup (Integer): The artist markup in percent, for example 20
        represents a 20% markup.
        _quantity (Integer): The quantity of this item.

    """

    def __init__(self, product_type:str, options:json, artist_markup:int, quantity: int):
        """
        Constructor for the CartItem Class.

        Args:
            self (none): None.
            product_type (String): The Type of the CartItem Being Purchased.
            options (Key-value pairs of strings.): Options that the CartItem
            Falls Under.
            artist_markup (Integer): The artist markup in percent, for example
            20 represents a 20% markup.
            quantity (Integer): The quantity of this item.

        Returns:
            (void): No return value. Just sets member variables.
        """
        self._product_type = product_type
        self._options = options
        self._artist_markup = artist_markup
        self._quantity = quantity
        # self._base_price = base_price

    def get_product_type(self):
        """
        Public Accessor for the Member Variable: CartItem Type.

        Args:
            self (none): None.
        Returns:
            (String): The Type of the CartItem Being Purchased.
        """
        return self._product_type

    def get_options(self):
        """
        Public Accessor for the Member Variable: Options.

        Args:
            self (none): None.
        Returns:
            (Key-value pairs of strings.): Options that the CartItem Falls
            Under.
        """
        return self._options

    def get_artist_markup(self):
        """
        Public Accessor for the Member Variable: Artist Markup.

        Args:
            self (none): None.
        Returns:
            (Integer): The artist markup in percent, for example 20 represents a
            20% markup.
        """
        return self._artist_markup

    def get_quantity(self):
        """
        Public Accessor for the Member Variable: Quantity.

        Args:
            self (none): None.
        Returns:
            (Integer): The quantity of this item.
        """
        return self._quantity

class Cart:
    """
    Cart Class - Represents a Shopping Cart.

    Attributes:
        _cart_json (JSON Object): JSON Object Represented in the Cart JSON File.
        _self._product_counts (Dictionary): Key - CartItem Type | Value - Quantity
        _list_of_items (List): Contains CartItems in a List.
    """

    def __init__(self, cart_json):
        """
        Constructor for the Cart Class.

        Args:
            self (none): None.
            cart_json (JSON Object): JSON Object Represented in the Cart JSON File.

        Returns:
            (void): No return value. Just sets member variables.
        """
        self._cart_json = cart_json  # Can Be Useful in Future
        self._product_counts = {}
        self._list_of_items = self.transform_to_cart_items(cart_json)

    def transform_to_cart_items(self, cart_json):
        """
        Retrieves the CartItems from the Cart Json File.

        Args:
            self (none): None.
            cart_json (JSON Object): JSON Object Represented in the Cart JSON
            File.
        Returns:
            (List): Contains CartItems in a List.
        """
        rs = []
        for product in cart_json:
            # From Cart Schema (THIS MAY CHANGE), we need Required properties : CartItem Type, Options, Artist-Markup,
            # and Quantity
            new_product = CartItem(
                product_type=product['product-type'],
                options=product['options'],
                artist_markup=product['artist-markup'],
                quantity=product['quantity']
            )

            rs.append(new_product)
        return rs

    def get_product_items(self):
        """
        Public Accessor for the Member Variable: CartItems List.
        *More Memory Efficient for CartItems if make_product_items() was
        already called.*

        Args:
            self (none): None.
        Returns:
            (List): Contains CartItems in a List.
        """
        return self._list_of_items

    def get_cart_json(self):
        """
        Public Accessor for the Member Variable: Cart_Json - JSON Object.

        Args:
            self (none): None.
        Returns:
            (JSON Object): JSON Object Represented in the Cart JSON
            File.
        """
        return self._cart_json

class PriceFinder:
    """
    PriceFinder is a Price Lookup class for CartItems.

    Attributes:
        _price_json (JSON Object): JSON Object Represented in the Base Price
        JSON File.
    """

    def __init__(self, price_json: json):
        """
        Constructor for the PriceFinder Class.

        Args:
            self (none): None.
            price_json (JSON Object): JSON Object Represented in the Base Price
            JSON File.

        Returns:
            (void): No return value. Just sets member variables.
        """
        self._price_json = price_json
        self.base_prices = {}

    def get_price_json(self):
        """
        Public Accessor for the Member Variable: Price_Json - JSON Object.

        Args:
            self (none): None.
        Returns:
            (JSON Object): JSON Object Represented in the Base Price JSON
            File.
        """
        return self._price_json

    def get_price_point(self, product):
        """
        Returns the Price of a CartItem in relation to the CartItem's
        attributes.

        Args:
            self (none): None.
            product (CartItem): Represents a CartItem in the Redbubble
            Shopping Cart.
        Returns:
            (Integer): The Price of the CartItem in Cents. Sentinel: Returns -1
            if ERROR and Price Cannot Be Found.
        """
        base_price = -1

        for price in self._price_json:

            if product.get_product_type() == price['product-type']:
                # We MAY Have a Match - Need to Check If Options Are the Same
                match = False  # Guilty until proven innocent!
                product_options = product.get_options()
                price_options = price['options']
                for option in price_options:
                    if product_options[option] not in price_options[option]:
                        match = True
                        break
                if not match:
                    base_price = price['base-price']
                    break

        price = (base_price + round(base_price * product.get_artist_markup() / 100)) * product.get_quantity()
        return int(price)

class Calculator:
    """
    Calculator Class for CartItems in the RedBubble
    Shopping Cart.
    """
    pass