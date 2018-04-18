require 'database'
require 'test/unit'

# tests the product database
class TestDatabase < Test::Unit::TestCase
  def test_loading
    db = Database.new
    sugar = db.get_product('sugar')
    assert_not_nil(sugar)
    assert_equal(0.65, sugar['price'])
    assert_equal(0.07, sugar['taxRate'])
    assert_not_nil(db.get_product('red wine'))
  end
end
