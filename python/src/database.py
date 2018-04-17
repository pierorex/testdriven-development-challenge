import json

class Database:
    def __init__(self, fileName="../products.json"):
        with open(fileName) as f:
            products = json.load(f)
        self.products_by_id = {p['productId'] : p for p in products}

    def get_product(self, product_id):
        return self.products_by_id[product_id]
