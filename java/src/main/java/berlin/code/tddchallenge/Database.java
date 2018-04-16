package berlin.code.tddchallenge;

import berlin.code.tddchallenge.data.Product;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.io.InputStream;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class Database {

    /**
     * Maps the product ID to a product which contains pricing and taxes data
     */
    private final Map<String, Product> products;

    public Database() throws IOException {
        this("products.json");
    }

    public Database(String fileName) throws IOException {
        products = loadData(fileName);
    }

    /**
     * loads product data from a json file.
     */
    private static Map<String, Product> loadData(String fileName) throws IOException {
        Map<String, Product> products = new HashMap<>();

        try (InputStream in = ClassLoader.getSystemClassLoader().getResourceAsStream(fileName)) {
            for (Product product : new ObjectMapper().readValue(in, Product[].class)) {
                products.put(product.getProductId(), product);
            }
        }

        return Collections.unmodifiableMap(products);
    }

    /**
     * @return a mapping of product ids to products
     */
    public Map<String, Product> getProducts() {
        return products;
    }

    /**
     * @return a product for the specified id or null
     */
    public Product getProduct(String productId) {
        return products.get(productId);
    }

    @Override
    public String toString() {
        return String.format("Database{products=%s}", products);
    }
}
