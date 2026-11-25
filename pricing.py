def calculate_subtotal(items):
    subtotal = 0

    for item in items:
        subtotal += item["quantity"] * item["price"]

    return subtotal


def calculate_discount(subtotal, customer_type):

    if customer_type == "premium":
        discount = subtotal * 0.10

    elif customer_type == "regular":
        discount = subtotal * 0.05

    else:
        discount = 0

    return discount