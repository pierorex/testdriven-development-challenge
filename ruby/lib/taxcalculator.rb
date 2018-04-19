# frozen_string_literal: true

# calculate taxes for a shopping cart
class TaxCalculator
  def initialize(database, shopping_cart)
    @database = database
    @shopping_cart = shopping_cart
  end

  def grandtotal
    0  # TODO
  end

  def grandtotal_tax(tax_rate)
    0  # TODO
  end

  def subtotal(tax_rate)
    0  # TODO
  end

  def subtotal_tax(tax_rate)
    0  # TODO
  end
end
