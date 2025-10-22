import os
from typing import Union

from fastapi import FastAPI

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
DB_URL = os.getenv("DB_URL")

# Create FastAPI app instance
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}