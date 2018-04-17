package berlin.code.tddchallenge.test;

import berlin.code.tddchallenge.Database;
import berlin.code.tddchallenge.TaxCalculator;
import berlin.code.tddchallenge.data.ShoppingCart;
import berlin.code.tddchallenge.data.ShoppingCartItem;
import org.junit.jupiter.api.*;

import java.io.IOException;

import static org.junit.jupiter.api.Assertions.*;

public class ShoppingExampleTest {
    private ShoppingCart cart;
    private Database db;

    @BeforeEach
    public void setup() throws IOException {
        db = new Database();
        cart = new ShoppingCart(
                new ShoppingCartItem("apple", 5),
                new ShoppingCartItem("orange", 4),
                new ShoppingCartItem("milk", 2),
                new ShoppingCartItem("red wine", 3),
                new ShoppingCartItem("stamps", 4)
        );
    }

    @Test
    public void productsAvailableTest() {
        for (ShoppingCartItem item : cart.getContents()) {
            assertNotNull(db.getProduct(item.getProductId()), "product lookup failed for " + item);
        }
    }

    @Test
    public void taxCalculatorTest() {
        TaxCalculator calc = new TaxCalculator(db, cart);

        // TODO write integration test

        assertEquals(2.89, calc.getSubtotalTax(.07), 0.005, "unexpected subtotal for 7%");
    }
}
