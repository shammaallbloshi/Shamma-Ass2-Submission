from invoice import Invoice


def test_invoice():
    invoice = Invoice(5001, 1001, 101, 15.99, "2024-10-29")

    # Generate and print the invoice
    invoice.print_invoice()


test_invoice()