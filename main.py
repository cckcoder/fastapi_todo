from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hello_world():
    return {'hello': 'world'}


@app.get("/items/{item_id}")
def get_items_by_id(item_id: int):
    return {'item_id': f'Hello item no {item_id}'}
