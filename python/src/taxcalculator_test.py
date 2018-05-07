import pytest

from database import Database
from taxcalculator import TaxCalculator, NonPositiveProductQuantity, NotIntegerProductQuantity, ShoppingCartIsNotList


def get_shopping_cart():
    return [
        {"productId": "apple", "quantity": 5},
        {"productId": "orange", "quantity": 4},
        {"productId": "milk", "quantity": 2},
        {"productId": "red wine", "quantity": 3},
        {"productId": "stamps", "quantity": 4},
    ]


# TODO:
# def test_get_receipt():
#     """ check that we're able to create receipts as requested by the challenge"""
#     db = Database()
#     calc = TaxCalculator(db, get_shopping_cart())


def test_cart_is_list():
    db = Database()
    with pytest.raises(ShoppingCartIsNotList):
        TaxCalculator(db, {"productId": "orange", "quantity": 5})


def test_negative_product_quantities():
    """ check that we're able to raise exceptions in case of invalid quantities"""
    db = Database()
    with pytest.raises(NonPositiveProductQuantity):
        TaxCalculator(db, [{"productId": "orange", "quantity": 5}, {"productId": "apple", "quantity": -5}])
    with pytest.raises(NonPositiveProductQuantity):
        TaxCalculator(db, [{"productId": "orange", "quantity": 0}, {"productId": "apple", "quantity": 5}])


def test_integer_product_quantities():
    """ check that we're able to raise exceptions in case of invalid quantities"""
    db = Database()
    with pytest.raises(NotIntegerProductQuantity):
        TaxCalculator(db, [{"productId": "orange", "quantity": 3.5}, {"productId": "apple", "quantity": 5}])


def test_shopping_cart_in_db():
    """ check that we have all products of the shopping cart in the database"""
    db = Database()
    for item in get_shopping_cart():
        assert db.get_product(item['productId']) is not None


def test_get_subtotal_price():
    """ check that we're able to calculate subtotal prices"""
    db = Database()
    calc = TaxCalculator(db, get_shopping_cart())
    assert round(calc.get_subtotal(0.07), 2) == 9.98
    assert round(calc.get_subtotal(0.19), 2) == 20.97


def test_get_subtotal_price_empty_taxclass():
    """ check subtotals of empty tax classes is 0.0"""
    db = Database()
    calc = TaxCalculator(db, get_shopping_cart())
    assert round(calc.get_subtotal(1.0), 2) == 0.00


def test_get_subtotal_tax():
    """ check that we're able to calculate subtotal taxes"""
    db = Database()
    calc = TaxCalculator(db, get_shopping_cart())
    assert round(calc.get_subtotal_tax(0.19), 2) == 3.35
    assert round(calc.get_subtotal_tax(0.07), 2) == 0.65


def test_get_subtotal_tax_empty_taxclass():
    """ check that we're able to calculate subtotal taxes for empty tax classes"""
    db = Database()
    calc = TaxCalculator(db, get_shopping_cart())
    assert round(calc.get_subtotal_tax(1.0), 2) == 0.00


def test_valid_products():
    """ check valid products are actually valid"""
    db = Database()
    calc = TaxCalculator(db, get_shopping_cart())
    expected_valid_products = [{"productId": "apple", "quantity": 5}, {"productId": "orange", "quantity": 4}, {"productId": "milk", "quantity": 2}]
    assert calc.valid_products(0.07) == expected_valid_products


def test_valid_products_empty_taxclass():
    """ check valid products are actually valid"""
    db = Database()
    calc = TaxCalculator(db, get_shopping_cart())
    expected_valid_products = []
    assert calc.valid_products(1.0) == expected_valid_products


def test_get_tax_rates():
    """ check we get correct tax rates from db"""
    db = Database()
    calc = TaxCalculator(db, get_shopping_cart())
    assert calc.get_tax_rates() == {0.07, 0.19, 0.0}


def test_get_grandtotal():
    """ check that we're able to calculate grandtotal prices"""
    db = Database()
    calc = TaxCalculator(db, get_shopping_cart())
    assert round(calc.get_grandtotal(), 2) == 33.55


def test_get_grandtotal_tax():
    """ check that we're able to calculate grandtotal tax"""
    db = Database()
    calc = TaxCalculator(db, get_shopping_cart())
    assert round(calc.get_grandtotal_tax(), 2) == 4.0
