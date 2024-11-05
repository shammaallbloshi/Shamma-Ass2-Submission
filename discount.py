class Discount:
    """Represents a discount applied to an order."""

    def _init_(self, discount_id, description, percentage):
        self.__discount_id = discount_id
        self.__description = description
        self.__percentage = percentage

    def apply_discount(self, price):
        """Applies the discount to the given price."""
        return price * (1 - self.__percentage / 100)

    def _str_(self):
        return f"Discount ID: {self._discount_id}, Description: {self.description}, Percentage: {self._percentage}%"