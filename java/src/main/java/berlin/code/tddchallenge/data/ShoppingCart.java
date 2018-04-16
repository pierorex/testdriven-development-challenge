package berlin.code.tddchallenge.data;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class ShoppingCart {

    private List<ShoppingCartItem> contents;

    public ShoppingCart() {
        contents = Collections.emptyList();
    }

    public ShoppingCart(List<ShoppingCartItem> contents) {
        this.contents = Collections.unmodifiableList(contents);
    }

    public ShoppingCart(ShoppingCartItem... contents) {
        this.contents = Arrays.asList(contents);
    }

    public List<ShoppingCartItem> getContents() {
        return contents;
    }

    public void setContents(List<ShoppingCartItem> contents) {
        this.contents = contents;
    }

    @Override
    public String toString() {
        return String.format("ShoppingCart{contents=%s}", contents);
    }
}
