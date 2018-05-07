class NonPositiveProductQuantity(BaseException):
    pass


class NotIntegerProductQuantity(BaseException):
    pass


class ShoppingCartIsNotList(BaseException):
    pass


class ProductInCartWithoutQuantity(BaseException):
    pass


class TaxCalculator:
    def __init__(self, db, shopping_cart):
        self.db = db
        self.shopping_cart = shopping_cart

        if type(shopping_cart) != list: raise ShoppingCartIsNotList

        # validate quantities type and range
        for p in self.shopping_cart:
            try:
                if type(p['quantity']) != int: raise NotIntegerProductQuantity
                if p['quantity'] < 1: raise NonPositiveProductQuantity
            except KeyError:
                if p.get('quantity') is None: raise ProductInCartWithoutQuantity

    def get_tax_rates(self):
        """
        Get tax_rates of the products existing in the shopping cart, without duplicates
        :return: set of tax_rates existing in the shopping cart
        :rtype: set
        """
        return set([self.db.get_product(p['productId'])['taxRate'] for p in self.shopping_cart])

    def _get_grandtotal_helper(self, f):
        """
        Helper function for the get_grandtotal and get_grandtotal_tax computations
        :param function f: function to be applied in the calculations
        :return: sum of the outputs of the function over the different tax_rate classes
        :rtype: float
        """
        return sum([f(tax_rate) for tax_rate in self.get_tax_rates()])

    def get_grandtotal(self):
        """
        Compute total amount of money to pay (VAT included)
        :return: total tax to pay by the customer (including VAT)
        :rtype: float
        """
        return self._get_grandtotal_helper(self.get_subtotal)

    def get_grandtotal_tax(self):
        """
        Compute total amount of tax to pay
        :return: total tax to pay by the customer (including VAT)
        :rtype: float
        """
        return self._get_grandtotal_helper(self.get_subtotal_tax)

    def valid_products(self, tax_rate):
        """
        Lists all products in self.shopping_cart that belong to the given tax_rate class
        :param float tax_rate: class/type of tax_rate applied to the product's price
        :return: list of products
        :rtype: list
        """
        return [p for p in self.shopping_cart if tax_rate == self.db.get_product(p['productId'])['taxRate']]

    def get_subtotal(self, tax_rate):
        """
        Check which items belong to this tax_rate in the cart and add up their prices
        :param float tax_rate: class/type of tax_rate applied to the product's price
        :return: sum of all the prices in this particular tax_rate class
        :rtype: float
        """
        valid_products = self.valid_products(tax_rate)
        agg_prices = sum([p['quantity'] * self.db.get_product(p['productId'])['price'] for p in valid_products])
        return agg_prices

    def get_subtotal_tax(self, tax_rate):
        """
        Check which items belong to this tax_rate in the cart and add up their taxes
        :param float tax_rate: class/type of tax_rate applied to the product's price
        :return: sum of all the taxes in this particular tax_rate class
        :rtype: float
        """
        return tax_rate * self.get_subtotal(tax_rate) / (1 + tax_rate)
