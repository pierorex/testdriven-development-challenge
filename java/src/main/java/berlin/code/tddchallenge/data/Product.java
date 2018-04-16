package berlin.code.tddchallenge.data;

public class Product {
    private String productId;
    private double price;
    private double taxRate;

    public String getProductId() {
        return productId;
    }

    public void setProductId(String productId) {
        this.productId = productId;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public double getTaxRate() {
        return taxRate;
    }

    public void setTaxRate(double taxRate) {
        this.taxRate = taxRate;
    }

    @Override
    public String toString() {
        return String.format("Product{productId='%s', price=%s, taxRate=%s}", productId, price, taxRate);
    }
}
