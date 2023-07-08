from fastapi import FastAPI, Request, HTTPException
from pymongo import MongoClient
from datetime import datetime
import uuid

app = FastAPI()

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client["ecommerce"]
products_collection = db["products"]
orders_collection = db["orders"]

# API to list all available products
@app.get("/products")
def get_products():
    products = list(products_collection.find({}, {"_id": 0}))
    return {"products": products}

# API to create a new order
@app.post("/orders")
def create_order(order: dict):

    # check the order data
    required_fields = ["items", "user_address"]
    for field in required_fields:
        if field not in order:
            raise HTTPException(status_code=400, detail=f"Missing required field: {field}")

    total_amount = 0.0
    for item in order["items"]:
        # Retrieve product details from MongoDB collection
        product = products_collection.find_one({"product_id": item["product_id"]})
        if not product:
            raise HTTPException(status_code=400, detail=f"Product not found with product_id: {item['product_id']}")
        if item["boughtQuantity"] > product["quantity"]:
            raise HTTPException(status_code=400, detail=f"Insufficient quantity for product: {product['name']}")
        total_amount += product["price"] * item["boughtQuantity"]

    # Generate a unique order ID
    order_id = str(uuid.uuid4())

    # Create order document
    new_order = {
        "order_id": order_id,
        "timestamp": datetime.now(),
        "items": order["items"],
        "total_amount": total_amount,
        "user_address": order["user_address"]
    }

    # Insert the new order into the MongoDB collection
    inserted_order = orders_collection.insert_one(new_order)
    return {"message": "Order created successfully", "order_id": str(inserted_order.inserted_id), "total_amount": total_amount}

# API to list all orders
@app.get("/orders")
def get_orders(limit: int = 10, offset: int = 0):
    # Retrieve all orders from the MongoDB collection
    orders = list(orders_collection.find({}, {"_id": 0}))
    return orders

# API to fetch a single order by Order ID
@app.get("/orders/{order_id}")
def get_order(order_id: str):
    # Retrieve a single order by Order ID from the MongoDB collection
    order = orders_collection.find_one({"order_id": order_id}, {"_id": 0})
    if order:
        return order
    else:
        raise HTTPException(status_code=404, detail="Order not found")

# API to update product available quantity
@app.put("/products/{product_id}")
def update_product(product_id: int, quantity: int):
    # Update the available quantity of a product in the MongoDB collection
    result = products_collection.update_one({"product_id": product_id}, {"$set": {"quantity": quantity}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product updated successfully"}
