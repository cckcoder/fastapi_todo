from fastapi import FastAPI
from typing import Optional


app = FastAPI()


@app.get("/")
def hello_world():
    return {'hello': 'world'}


@app.get("/items/{item_id}")
def get_items_by_id(item_id: int, q: Optional[str] = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': f'Hello item no {item_id}'}
