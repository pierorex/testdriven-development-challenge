package berlin.code.tddchallenge.test;

import berlin.code.tddchallenge.Database;
import org.junit.jupiter.api.*;

import java.io.IOException;

import static org.junit.jupiter.api.Assertions.*;

public class DatabaseTest {

    @Test
    public void testLoadingProducts() throws IOException {
        Database db = new Database();
        assertEquals(19, db.getProducts().size(), "product count in database is incorrect");
        assertEquals(0.65, db.getProduct("sugar").getPrice(), "price for sugar");
        assertEquals(0.07, db.getProduct("sugar").getTaxRate(), "tax rate for sugar");
        assertNotNull(db.getProduct("red wine"), "support for spaces in product id");
    }

    @Test
    public void testLoadingFail() throws IOException {
        try {
            new Database("invalid-name.jpg");
            fail("invalid filename should have caused an IOException");
        } catch(IOException expected) {
            // expected to fail with an IOException
        }
    }


}
