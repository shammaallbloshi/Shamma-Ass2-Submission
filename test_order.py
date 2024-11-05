from order import Order
from shopping_cart import ShoppingCart
from ebook import EBook


def test_order():
    # Set up shopping cart and order
    cart = ShoppingCart(1, 101)
    book1 = EBook(101, "1984", "George Orwell", 15.99, "Dystopian", 50)
    cart.add_item(book1)

    order = Order(1001, 101, cart, "123 Elm Street")

    # Place the order
    print(order.place_order())

    # Display order details
    print(order.display_order_details())


test_order()