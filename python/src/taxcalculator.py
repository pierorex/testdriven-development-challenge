class TaxCalculator:
    def __init__(self, db, shopping_cart):
        self.db = db
        self.shopping_cart = shopping_cart

    def get_tax_rates(self):
        return set([self.db.get_product(p['productId'])['taxRate'] for p in self.shopping_cart])

    def get_grandtotal(self):
        return sum([self.get_subtotal(tax_rate) for tax_rate in self.get_tax_rates()])

    def get_grandtotal_tax(self):
        return sum([self.get_subtotal_tax(tax_rate) for tax_rate in self.get_tax_rates()])

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
        return tax_rate * self.get_subtotal(tax_rate)
