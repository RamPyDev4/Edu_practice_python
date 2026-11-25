
from inventory_repository import get_inventory_by_product


def calculate_total_stock(product_id):
    product_inventory = get_inventory_by_product(product_id)

    total_stock = 0

    for item in product_inventory:
        total_stock += item["quantity"]

    return total_stock
