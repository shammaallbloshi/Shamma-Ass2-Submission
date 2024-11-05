from customer import Customer

def test_customer():
    customer = Customer(1, "afra", "afra@gmail.com", "45 Street")

    print(customer.register_customer())
    print(customer)

    # Update account info
    print(customer.update_account_info(name="afra", email="afra@gmail.com"))

    # View orders (expecting no orders)
    print(customer.view_orders())

test_customer()