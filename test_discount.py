from discount import Discount


def test_discount():
    # Create a discount of 10%
    discount = Discount(1, "Loyalty Program Discount", 10)

    # Apply discount to a price of $100
    original_price = 100.00
    discounted_price = discount.apply_discount(original_price)

    # Display results
    print(f"Original Price: ${original_price:.2f}")
    print(f"Discounted Price: ${discounted_price:.2f}")

    # Test another discount of 20%
    bulk_discount = Discount(2, "Bulk Purchase Discount", 20)
    bulk_discounted_price = bulk_discount.apply_discount(original_price)

    print(f"Bulk Discounted Price: ${bulk_discounted_price:.2f}")


test_discount()