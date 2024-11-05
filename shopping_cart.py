class ShoppingCart:
    """Represents a customer's shopping cart."""

    def _init_(self, cart_id, customer_id):
        self.__cart_id = cart_id
        self.__customer_id = customer_id
        self.__items = []

    def add_item(self, ebook):
        """Adds an eBook to the cart."""
        self.__items.append(ebook)

    def remove_item(self, ebook):
        """Removes an eBook from the cart."""
        if ebook in self.__items:
            self.__items.remove(ebook)

    def calculate_total(self):
        """Calculates the total price of the items in the cart."""
        return sum([item.get_price() for item in self.__items])

    def _str_(self):
        return f"Cart ID: {self._cart_id}, Total Items: {len(self._items)}"
