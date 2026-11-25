
from fastapi import FastAPI
from order_service import get_delivered_orders
from inventory_service import calculate_total_stock


app = FastAPI()

@app.get("/customers/{customer_id}/orders")
def fetch_customer_orders(customer_id: int):
    result = get_delivered_orders(customer_id)

    return {
        "customer_id": customer_id,
        "total_orders": len(result),
        "orders": result
    }



@app.get("/products/{product_id}/stock")
def fetch_product_stock(product_id: int):
    total_stock = calculate_total_stock(product_id)

    return {
        "product_id": product_id,
        "total_stock": total_stock
    }
