class EBook:
    """Represents an eBook with its details."""

    def _init_(self, book_id, title, author, price, genre, stock_quantity):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__price = price
        self.__genre = genre
        self.__stock_quantity = stock_quantity

    def update_stock(self, quantity):
        """Updates the stock quantity of the eBook."""
        self.__stock_quantity += quantity

    def display_book_info(self):
        """Displays detailed information about the eBook."""
        return f"Title: {self._title}, Author: {self.author}, Price: ${self.price}, Genre: {self._genre}"

    def apply_discount(self, discount_percentage):
        """Applies a discount to the eBook price."""
        self.__price *= (1 - discount_percentage / 100)

    def get_price(self):
        """Returns the price of the eBook."""
        return self.__price

    def _str_(self):
        return f"ID: {self._book_id}, Title: {self.title}, Stock: {self._stock_quantity}"