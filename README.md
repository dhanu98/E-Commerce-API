# E-commerce API

This is an API for an e-commerce application built using FastAPI and MongoDB. It provides endpoints to manage products, create orders, and retrieve order details.

## Installation

- Python (3.10 or above)
- FastAPI
- MongoDB


## Usage

1. Run the application using `uvicorn main:app --reload` or `python main.py`.
2. The API will be available at `http://localhost:8000`.
3. Use a tool like Postman to interact with the API endpoints.

## Endpoints

- List all available products:
    - URL: `/products`
    - Method: GET

- Create a new order:
    - URL: `/orders`
    - Method: POST
    - Request body: Contains order details(Items, Quantity)

- List all orders:
    - URL: `/orders`
    - Method: GET

- Fetch a single order by Order ID:
    - URL: `/orders/{order_id}`
    - Method: GET

- Update product available quantity:
    - URL: `/products/{product_id}`
    - Method: PUT
    - Request body: Contains update details(Quantity)


