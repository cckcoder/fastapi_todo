from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Coffee(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    star: int

dummy_db = [
    {
        'name': 'Espresso',
        'description': 'เป็นกาแฟดำที่เข้มที่สุด เป็นจุดเริ่มต้นของกาแฟทุกแก้ว จะถูกเสิร์ฟในแก้วกาแฟร้อนที่เล็กๆ',
        'price': 60,
        'star': 5
    },
    {
        'name': 'Americano',
        'description': 'เป็นการเทกาแฟ Espresso 1 ช็อต  ตามด้วยน้ำร้อน หรือน้ำธรรมดา',
        'price': 55,
        'star': 5
    }
]


app = FastAPI()


@app.get("/")
def show_all_coffee():
    return dummy_db


@app.get("/coffee/{coffee_id}")
def get_items_by_id(coffee_id: int):
    coffee = dummy_db[coffee_id - 1]
    return coffee


@app.post("/coffee")
def create_coffee(coffee: Coffee):
    dummy_db.append(coffee)
    return dummy_db[-1]


@app.delete("/coffee/{coffee_id}")
def delete_coffee(coffee_id: int):
    coffee = dummy_db[coffee_id - 1]
    dummy_db.pop(coffee_id - 1)
    result = {'msg': f"{coffee['name']} was delete!"}
    return result

