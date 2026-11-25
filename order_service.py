from pricing import calculate_subtotal, calculate_discount


def generate_invoice(order):

    order_id = order["order_id"]
    customer_type = order["customer_type"]

    subtotal = calculate_subtotal(order["items"])

    discount = calculate_discount(subtotal, customer_type)

    final_amount = subtotal - discount

    return {
        "order_id": order_id,
        "customer_type": customer_type,
        "subtotal": subtotal,
        "discount": discount,
        "final_amount": final_amount
    }