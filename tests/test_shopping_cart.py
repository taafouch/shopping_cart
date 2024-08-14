from __future__ import print_function, division
import pytest
from shopping_cart.cart import ShoppingCart


@pytest.fixture
def cart():
    """Create a new ShoppingCart instance for each test."""
    return ShoppingCart()


def test_add_item(cart):
    """Test adding items to the cart."""
    cart.add_item("apple", 0.5, 2)
    assert cart.get_item("apple") == {"price": 0.5, "quantity": 2}
    assert cart.get_total_items() == 2
    assert cart.get_total_price() == 1.00

    cart.add_item("banana", 0.75, 3)
    assert cart.get_item("banana") == {"price": 0.75, "quantity": 3}
    assert cart.get_total_items() == 5
    assert cart.get_total_price() == 3.25


# ... (rest of the test functions remain largely the same)


def test_remove_item(cart):
    """Test removing items from the cart."""
    cart.add_item("apple", 0.5, 3)
    cart.remove_item("apple", 2)
    assert cart.get_item("apple") == {"price": 0.5, "quantity": 1}
    assert cart.get_total_items() == 1
    assert cart.get_total_price() == 0.50

    cart.remove_item("apple")
    assert cart.get_item("apple") is None
    assert cart.get_total_items() == 0
    assert cart.get_total_price() == 0.00


def test_get_total_price(cart):
    """Test calculating the total price of items in the cart."""
    cart.add_item("apple", 0.5, 2)
    cart.add_item("banana", 0.75, 3)
    cart.add_item("orange", 0.6, 1)
    assert cart.get_total_price() == 3.85


def test_get_total_items(cart):
    """Test counting the total number of items in the cart."""
    cart.add_item("apple", 0.5, 2)
    cart.add_item("banana", 0.75, 3)
    assert cart.get_total_items() == 5


def test_invalid_inputs(cart):
    """Test handling of invalid inputs."""
    with pytest.raises(ValueError):
        cart.add_item("apple", -0.5)

    with pytest.raises(ValueError):
        cart.add_item("apple", 0.5, 0)

    with pytest.raises(ValueError):
        cart.remove_item("banana")

    cart.add_item("apple", 0.5, 2)
    with pytest.raises(ValueError):
        cart.remove_item("apple", 3)


def test_string_representation(cart):
    """Test the string representation of the cart."""
    cart.add_item("apple", 0.5, 2)
    cart.add_item("banana", 0.75, 3)
    expected_str = (
        "Shopping Cart:\n"
        "apple: 2 x $0.50\n"
        "banana: 3 x $0.75\n"
        "Total: $3.25"
    )
    assert str(cart) == expected_str
