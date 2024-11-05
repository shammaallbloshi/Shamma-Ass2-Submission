from shopping_cart import ShoppingCart
from ebook import EBook


def test_shopping_cart():
    cart = ShoppingCart(1, 101)

    # Add eBooks to the cart
    book1 = EBook(101, "1984", "George Orwell", 15.99, "Dystopian", 50)
    book2 = EBook(102, "To Kill a Mockingbird", "Harper Lee", 10.99, "Fiction", 30)

    cart.add_item(book1)
    cart.add_item(book2)

    # Remove an eBook
    cart.remove_item(book2)

    # Calculate total
    print(f"Cart Total: ${cart.calculate_total():.2f}")


test_shopping_cart()