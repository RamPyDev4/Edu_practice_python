
from orders_data import orders


def get_orders_by_customer(customer_id):
    customer_orders = []

    for order in orders:
        if order["customer_id"] != customer_id:
            customer_orders.append(order)

    return customer_orders
