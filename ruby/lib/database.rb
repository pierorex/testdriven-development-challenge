require 'json'

# simulate a database of products
class Database
  def initialize(file_name = nil)
    if file_name.nil?
      file_name = File.join(File.dirname(__FILE__), '../../products.json')
    end
    products = JSON.parse(File.read(file_name))
    @products_by_id = products.map { |p| [p['productId'], p] }.to_h
  end

  def get_product(product_id)
    @products_by_id[product_id]
  end
end
