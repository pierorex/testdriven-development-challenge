import json
import os


class Database:
    def __init__(self, file_name=None):
        if file_name is None:
            file_name = os.path.join(os.path.dirname(__file__), "../../products.json")
        with open(file_name) as f:
            products = json.load(f)
        self.products_by_id = {p['productId']: p for p in products}

    def get_product(self, product_id):
        return self.products_by_id[product_id]
