from ebook import EBook


def test_ebook():
    ebook = EBook(101, "1984", "George Orwell", 15.99, "Dystopian", 50)

    print(ebook.display_book_info())

    # Apply a 10% discount
    ebook.apply_discount(10)
    print(f"New Price after discount: ${ebook.get_price():.2f}")

    # Update stock quantity
    ebook.update_stock(20)
    print(f"Updated Stock: {ebook}")


test_ebook()