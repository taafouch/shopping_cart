from __future__ import print_function, division
import six


class ShoppingCart(object):
    """A class to manage a shopping cart with items and their prices."""

    def __init__(self):
        """Initialize an empty shopping cart."""
        self._items = {}

    def add_item(self, item_name, price, quantity=1):
        """Add an item to the shopping cart."""
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        rounded_price = round(price, 2)
        if item_name in self._items:
            self._items[item_name]["quantity"] += quantity
        else:
            self._items[item_name] = {"price": rounded_price, "quantity": quantity}

    def remove_item(self, item_name, quantity=1):
        """Remove an item from the shopping cart."""
        if item_name not in self._items:
            raise ValueError("Item '{}' is not in the cart.".format(item_name))
        if quantity <= 0:
            raise ValueError("Quantity to remove must be positive.")
        if quantity > self._items[item_name]["quantity"]:
            raise ValueError("Not enough '{}' in the cart to remove.".format(item_name))

        self._items[item_name]["quantity"] -= quantity
        if self._items[item_name]["quantity"] == 0:
            del self._items[item_name]

    def get_item(self, item_name):
        """Get information about a specific item in the cart."""
        return self._items.get(item_name)

    def get_total_items(self):
        """Get the total number of items in the cart."""
        return sum(item["quantity"] for item in six.itervalues(self._items))

    def get_total_price(self):
        """Calculate the total price of all items in the cart."""
        total = sum(item["price"] * item["quantity"] for item in six.itervalues(self._items))
        return round(total, 2)

    def __str__(self):
        """Return a string representation of the shopping cart."""
        items_str = "\n".join(
            "{item_name}: {quantity} x ${price}".format(item_name=name,
                                                        quantity=item['quantity'],
                                                        price=item['price'])
            for name, item in six.iteritems(self._items)
        )
        return "Shopping Cart:\n{item}\nTotal: ${price}".format(item=items_str, price=self.get_total_price())
