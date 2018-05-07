import json
import os


class NonFloatProductPrice(BaseException):
    pass


class NonFloatProductTaxRate(BaseException):
    pass


class NegativeProductPrice(BaseException):
    pass


class NegativeProductTaxRate(BaseException):
    pass


class ProductInDbWithoutPrice(BaseException):
    pass


class ProductInDBWithoutTaxRate(BaseException):
    pass


class ProductInDbWithoutId(BaseException):
    pass


class Database:
    def __init__(self, file_name=None):
        if file_name is None:
            file_name = os.path.join(os.path.dirname(__file__), "../../products.json")
        with open(file_name) as f:
            products = json.load(f)
        try:
            self.products_by_id = {p['productId']: p for p in products}
        except KeyError: raise ProductInDbWithoutId

        # validate db records
        for k, v in self.products_by_id.items():
            try:
                if type(v['price']) != float: raise NonFloatProductPrice
                if type(v['taxRate']) != float: raise NonFloatProductTaxRate
                if v['price'] < 0: raise NegativeProductPrice
                if v['taxRate'] < 0: raise NegativeProductTaxRate
            except KeyError:
                if v.get('price') is None: raise ProductInDbWithoutPrice
                if v.get('taxRate') is None: raise ProductInDBWithoutTaxRate

    def get_product(self, product_id):
        return self.products_by_id[product_id]
