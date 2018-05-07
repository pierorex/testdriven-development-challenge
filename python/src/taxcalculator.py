class NonPositiveProductQuantity(BaseException):
    pass


class NotIntegerProductQuantity(BaseException):
    pass


class TaxCalculator:
    def __init__(self, db, shopping_cart):
        self.db = db
        self.shopping_cart = shopping_cart

        # validate quantities type and range
        for p in self.shopping_cart:
            print(type(p['quantity']))
            print(p['quantity'])
            if type(p['quantity']) != int:
                raise NotIntegerProductQuantity
            if p['quantity'] < 1:
                raise NonPositiveProductQuantity

    def get_tax_rates(self):
        return set([self.db.get_product(p['productId'])['taxRate'] for p in self.shopping_cart])

    def _get_grandtotal_helper(self, f):
        return sum([f(tax_rate) for tax_rate in self.get_tax_rates()])

    def get_grandtotal(self):
        return self._get_grandtotal_helper(self.get_subtotal)

    def get_grandtotal_tax(self):
        return self._get_grandtotal_helper(self.get_subtotal_tax)

    def valid_products(self, tax_rate):
        return [p for p in self.shopping_cart if tax_rate == self.db.get_product(p['productId'])['taxRate']]

    def get_subtotal(self, tax_rate):
        valid_products = self.valid_products(tax_rate)
        agg_prices = sum([p['quantity'] * self.db.get_product(p['productId'])['price'] for p in valid_products])
        return agg_prices

    def get_subtotal_tax(self, tax_rate):
        """
        Check which items belong to this tax_rate and add their prices
        :param tax_rate:
        :return:
        """
        return tax_rate * self.get_subtotal(tax_rate) / (1 + tax_rate)
