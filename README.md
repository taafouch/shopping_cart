# Shopping Cart Project

This project implements a simple shopping cart system in Python, allowing users to manage items, their quantities, and prices in a virtual shopping cart.

## Project Structure

```
shopping_cart/
│
├── shopping_cart/
│   ├── __init__.py
│   └── cart.py
│
├── tests/
│   └── test_shopping_cart.py
│
├── README.md
└── requirements.txt
```

## Features

- Add items to the cart with price and quantity
- Remove items from the cart
- Get information about a specific item
- Calculate the total number of items in the cart
- Calculate the total price of all items in the cart
- String representation of the cart contents

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/shopping-cart.git
   cd shopping-cart
   ```

2. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Here's a basic example of how to use the ShoppingCart class:

```python
from shopping_cart.cart import ShoppingCart

# Create a new shopping cart
cart = ShoppingCart()

# Add items to the cart
cart.add_item("apple", 0.5, 2)
cart.add_item("banana", 0.75, 3)

# Get information about an item
print(cart.get_item("apple"))

# Get the total number of items
print(cart.get_total_items())

# Get the total price
print(cart.get_total_price())

# Remove an item
cart.remove_item("apple", 1)

# Print the cart
print(cart)
```

## Running Tests

To run the tests, make sure you have pytest installed and then run:

```
pytest tests/test_shopping_cart.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
