import pytest

from database import Database, NegativeProductPrice, NonFloatProductPrice, NegativeProductTaxRate, \
    NonFloatProductTaxRate, ProductInDbWithoutPrice, ProductInDBWithoutTaxRate, ProductInDbWithoutId


def test_access_database():
    db = Database()
    sugar = db.get_product("sugar")
    assert sugar is not None
    assert sugar['price'] == 0.65
    assert sugar['taxRate'] == 0.07
    assert db.get_product("red wine") is not None


def test_all_valid_records():
    db = Database()
    for k, v in db.products_by_id.items():
        assert type(v.get('price')) == float
        assert type(v.get('taxRate')) == float
        assert v.get('productId') is not None
        assert v.get('price') >= 0.0000000
        assert v.get('taxRate') >= 0.000000


def test_db_products_is_dict():
    db = Database()
    assert type(db.products_by_id) == dict


def test_product_neg_price():
    with pytest.raises(NegativeProductPrice):
        db = Database('test_dbs/db_neg_price.json')


def test_product_neg_tax_rate():
    with pytest.raises(NegativeProductTaxRate):
        db = Database('test_dbs/db_neg_tax_rate.json')


def test_product_non_float_price():
    with pytest.raises(NonFloatProductPrice):
        db = Database('test_dbs/db_non_float_price.json')


def test_product_non_float_tax_rate():
    with pytest.raises(NonFloatProductTaxRate):
        db = Database('test_dbs/db_non_float_tax_rate.json')


def test_product_without_price():
    with pytest.raises(ProductInDbWithoutPrice):
        db = Database('test_dbs/db_without_price.json')


def test_product_without_tax_rate():
    with pytest.raises(ProductInDBWithoutTaxRate):
        db = Database('test_dbs/db_without_tax_rate.json')


def test_product_without_id():
    with pytest.raises(ProductInDbWithoutId):
        db = Database('test_dbs/db_without_id.json')
