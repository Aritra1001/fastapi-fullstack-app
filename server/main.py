from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Hello from the server"

# creating a sample list for products endpoint
products = [
    Product(id=1, name="Smart Phone", description="Budget phone", price=99, quantity=10),
    Product(id=2, name="Laptop", description="Gaming laptop", price=999, quantity=7),
    Product(id=3, name="Table", description="Wooden Table", price=50, quantity=12),
    Product(id=4, name="Office Chair", description="Reclining chair", price=60, quantity=5)
]

@app.get("/products")
def get_all_products():
    return products