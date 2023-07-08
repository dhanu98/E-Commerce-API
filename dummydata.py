from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]
products_collection = db["products"]

dummy_products = [
    {
        "product_id": 1,
        "name": "TV",
        "price": 499.99,
        "quantity": 10
    },
    {
        "product_id": 2,
        "name": "Laptop",
        "price": 999.99,
        "quantity": 5
    },
    {
        "product_id": 3,
        "name": "Smartphone",
        "price": 399.99,
        "quantity": 15
    },
    {
        "product_id": 4,
        "name": "Headphones",
        "price": 79.99,
        "quantity": 20
    },
    {
        "product_id": 5,
        "name": "Tablet",
        "price": 299.99,
        "quantity": 8
    },
    {
        "product_id": 6,
        "name": "Camera",
        "price": 649.99,
        "quantity": 12
    },
    {
        "product_id": 7,
        "name": "Gaming Console",
        "price": 499.99,
        "quantity": 7
    },
    {
        "product_id": 8,
        "name": "Smart Watch",
        "price": 199.99,
        "quantity": 18
    },
    {
        "product_id": 9,
        "name": "Bluetooth Speaker",
        "price": 89.99,
        "quantity": 15
    },
    {
        "product_id": 10,
        "name": "Wireless Earbuds",
        "price": 129.99,
        "quantity": 10
    },
    {
        "product_id": 11,
        "name": "Desktop Computer",
        "price": 1299.99,
        "quantity": 6
    },
    {
        "product_id": 12,
        "name": "Printer",
        "price": 199.99,
        "quantity": 9
    },
    {
        "product_id": 13,
        "name": "Monitor",
        "price": 299.99,
        "quantity": 12
    },
    {
        "product_id": 14,
        "name": "External Hard Drive",
        "price": 129.99,
        "quantity": 15
    },
    {
        "product_id": 15,
        "name": "Wireless Router",
        "price": 79.99,
        "quantity": 10
    },
    {
        "product_id": 16,
        "name": "Keyboard",
        "price": 49.99,
        "quantity": 20
    },
    {
        "product_id": 17,
        "name": "Mouse",
        "price": 29.99,
        "quantity": 25
    },
    {
        "product_id": 18,
        "name": "Power Bank",
        "price": 39.99,
        "quantity": 20
    },
    {
        "product_id": 19,
        "name": "Portable Speaker",
        "price": 59.99,
        "quantity": 15
    },
    {
        "product_id": 20,
        "name": "Fitness Tracker",
        "price": 79.99,
        "quantity": 10
    }
]

if products_collection.count_documents({}) == 0:
    products_collection.insert_many(dummy_products)