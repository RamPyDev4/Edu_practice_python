
from order_repository import get_orders_by_customer


def get_delivered_orders(customer_id):
    customer_orders = get_orders_by_customer(customer_id)

    delivered_orders = []

    for order in customer_orders:
        if order["status"] == "delivered":
            delivered_orders.append(order)

    return delivered_orders
