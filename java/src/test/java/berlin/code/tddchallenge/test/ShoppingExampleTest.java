package berlin.code.tddchallenge.test;

import berlin.code.tddchallenge.Database;
import berlin.code.tddchallenge.TaxCalculator;
import berlin.code.tddchallenge.data.ShoppingCart;
import berlin.code.tddchallenge.data.ShoppingCartItem;
import org.junit.jupiter.api.*;

import java.io.IOException;

import static org.junit.jupiter.api.Assertions.*;

public class ShoppingExampleTest {

    @Test
    public void shoppingTest() throws IOException {
        Database db = new Database();
        ShoppingCart cart = new ShoppingCart(
                new ShoppingCartItem("apple", 5),
                new ShoppingCartItem("orange", 4),
                new ShoppingCartItem("milk", 2),
                new ShoppingCartItem("red wine", 3),
                new ShoppingCartItem("stamps", 4)
        );

        for (ShoppingCartItem item : cart.getContents()) {
            assertNotNull(db.getProduct(item.getProductId()), "product lookup failed for " + item);
        }

        TaxCalculator calc = new TaxCalculator(db, cart);
        assertEquals(2.89, calc.getSubtotalTax(.07), 0.005, "unexpected subtotal for 7%");
    }
}
