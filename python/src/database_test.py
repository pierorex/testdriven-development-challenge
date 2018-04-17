from database import Database


def test_access_database():
    db = Database()
    sugar = db.get_product("sugar")
    assert sugar is not None
    assert sugar['price'] == 0.65
    assert sugar['taxRate'] == 0.07
    assert db.get_product("red wine") is not None
