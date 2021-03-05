from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel


router = APIRouter(
    prefix="/coffee",
    tags=['Coffee'],
    responses={404: {'message': "Not found"}}
)

class Coffee(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    star: int


coffee_db = [
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
    },
    {
        'name': 'Mocha',
        'description': 'กาแฟที่เกิดจากการผสมผสานของ ช็อต Espresso, Steamed Milk และ ช็อกโกแลต หรือ Mocha Syrup',
        'price': 65,
        'star': 4
    }
]


@router.get('/')
async def show_all_coffee():
    return coffee_db


@router.get("/{coffee_id}")
def coffee_by_id(coffee_id: int):
    coffee = coffee_db[coffee_id - 1]
    return coffee


@router.put("/{coffee_id}")
def update_coffee(coffee_id: int, coffee: Coffee):
    coffee_db[coffee_id - 1].update(**coffee.dict())
    result = {'msg': f"Coffee id {coffee_id} Update successfull"}
    return result



@router.post("")
def create_coffee(coffee: Coffee):
    coffee_db.append(coffee)
    return coffee_db[-1]


@router.delete("/{coffee_id}")
def delete_coffee(coffee_id: int):
    coffee = coffee_db[coffee_id - 1]
    coffee_db.pop(coffee_id - 1)
    result = {'msg': f"{coffee['name']} was delete!"}
    return result
