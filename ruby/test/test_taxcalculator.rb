# frozen_string_literal: true

require 'database'
require 'taxcalculator'
require 'test/unit'

# tests the tax calculator
class TestTaxCalculator < Test::Unit::TestCase
  def shopping_cart
    [
      {'productId' => 'apple', 'quantity' => 5},
      {'productId' => 'orange', 'quantity' => 4},
      {'productId' => 'milk', 'quantity' => 2},
      {'productId' => 'red wine', 'quantity' => 3},
      {'productId' => 'stamps', 'quantity' => 4},
    ]
  end

  def test_shopping_cart_in_db
    db = Database.new
    shopping_cart.each do |item|
      assert_not_nil(db.get_product(item['productId']))
    end
  end

  def test_calculation
    db = Database.new
    calc = TaxCalculator.new(db, shopping_cart)
    assert_equal(9.98, calc.subtotal_tax(0.07).round(2))
  end
end
