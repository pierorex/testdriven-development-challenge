from database import Database


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
        assert type(v.get('price')) == float
        assert v.get('productId') is not None
