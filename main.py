from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Path operation to handle GET requests
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Path operation to handle GET requests with path and query parameters
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Pydantic model to define the data structure for PUT request
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Path operation to handle PUT requests and update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}
