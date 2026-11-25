
from inventory_data import inventory


def get_inventory_by_product(product_id):
    product_inventory = []

    for item in inventory:
        if item["product_id"] == product_id:
            product_inventory.append(item)
            return product_inventory

    return product_inventory
