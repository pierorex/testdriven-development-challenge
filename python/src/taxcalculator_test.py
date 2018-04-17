from database import Database
from taxcalculator import TaxCalculator

shopping_cart = [
    {"productId": "apple", "quantity": 5},
    {"productId": "orange", "quantity": 4},
    {"productId": "milk", "quantity": 2},
    {"productId": "red wine", "quantity": 3},
    {"productId": "stamps", "quantity": 4},
]


def test_shopping_cart_in_db():
    """ check that we have all products of the shopping cart in the database"""
    db = Database()
    for item in shopping_cart:
        assert db.get_product(item['productId']) is not None


def test_calculation():
    """ check that we're able to calculate taxes and totals """
    db = Database()
    calc = TaxCalculator(db, shopping_cart)
    assert round(calc.get_subtotal_tax(0.07), 2) == 2.89
