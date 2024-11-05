from shopping_cart import ShoppingCart


class Order:
    """Represents a customer's order."""

    def _init_(self, order_id, customer_id, shopping_cart, shipping_address):
        self.__order_id = order_id
        self.__customer_id = customer_id
        self.__shopping_cart = shopping_cart
        self.__shipping_address = shipping_address
        self.__order_date = "2024-10-29"
        self._order_total = self._shopping_cart.calculate_total()

    def place_order(self):
        """Places an order and confirms it."""
        return f"Order {self._order_id} placed successfully. Total: ${self._order_total:.2f}"

    def cancel_order(self):
        """Cancels the order."""
        return f"Order {self.__order_id} has been canceled."

    def display_order_details(self):
        """Displays details of the order."""
        return f"Order ID: {self._order_id}, Total: ${self.order_total:.2f}, Date: {self._order_date}"

    def _str_(self):
        return f"Order ID: {self._order_id}, Customer ID: {self._customer_id}"