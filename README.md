# Shopping Cart Project

## Overview

The Shopping Cart Project is a Python-based utility that implements a simple shopping cart system. It allows users to manage items, their quantities, and prices in a virtual shopping cart. The project provides both a user-friendly class interface and a comprehensive test suite to ensure reliability.

## Features

- Add items to the cart with price and quantity
- Remove items from the cart
- Get information about a specific item
- Calculate the total number of items in the cart
- Calculate the total price of all items in the cart
- String representation of the cart contents
- Comprehensive test suite using pytest
- Prices are float values with two decimal places
- Error handling for invalid inputs

## Installation

1. Clone or download this repository to your local machine.
2. Navigate to the project directory:
   ```
   cd shopping-cart
   ```
3. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Using the ShoppingCart class

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

### Running Tests

To run the unit tests:

1. Ensure you have pytest installed:
   ```
   pip install pytest
   ```

2. Navigate to the project's root directory.

3. Run the tests using:
   ```
   pytest tests/test_shopping_cart.py
   ```

## Development

### Prerequisites

- Python 2.7 or 3.6+
- pytest for running tests

### Project Structure

```
shopping_cart/
│
├── src/
│   └── shopping_cart/
│       ├── __init__.py
│       └── cart.py
│
├── tests/
│   └── test_shopping_cart.py
│
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

## Contributing

Contributions to the Shopping Cart Project are welcome! Please feel free to submit a Pull Request.

### Guidelines for contributing:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Write tests for your changes.
4. Ensure all tests pass before submitting a pull request.
5. Update the documentation if you're introducing new features or changing functionality.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Python
- pytest for testing framework

## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.

## Authors

[Mohamed El Wafi]

---

We hope this project serves as a useful example of implementing a shopping cart system in Python. Happy coding!
