class Customer:
    """Represents a customer with personal and account details."""

    def _init_(self, customer_id, name, email, shipping_address):
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__shipping_address = shipping_address
        self.__orders = []  # To keep track of orders made by the customer

    def register_customer(self):
        """Registers a new customer."""
        return f"Customer {self.__name} registered successfully."

    def update_account_info(self, name=None, email=None, shipping_address=None):
        """Updates the customer account information."""
        if name:
            self.__name = name
        if email:
            self.__email = email
        if shipping_address:
            self.__shipping_address = shipping_address
        return "Account information updated successfully."

    def view_orders(self):
        """Displays the orders placed by the customer."""
        if self.__orders:
            return self.__orders
        return "No orders found for this customer."

    def add_order(self, order):
        """Adds an order to the customer's order history."""
        self.__orders.append(order)

    def _str_(self):
        return f"Customer ID: {self._customer_id}, Name: {self.name}, Email: {self._email}"