from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel


router = APIRouter(
    prefix="/staff",
    tags=['Staff'],
    responses={404: {'message': "Not found"}}
)


class Staff(BaseModel):
    name: str


staff_db = [
    {
        'name': 'John Doe',
    },
    {
        'name': 'Dylan Klye',
    }
]


@router.get('/')
async def show_all_coffee():
    return staff_db


@router.get("/{staff_id}")
def get_items_by_id(coffee_id: int):
    coffee = staff_db[coffee_id - 1]
    return coffee


@router.post("")
def create_coffee(staff: Staff):
    staff_db.append(staff)
    return staff_db[-1]


@router.put("/{staff_id}")
def delete_coffee(staff_id: int, staff: Staff):
    staff_db[staff_id - 1].update(**staff.dict())
    result = {'msg': "Update successfull"}
    return result


@router.delete("/{staff_id}")
def delete_coffee(staff_id: int):
    staff = staff_db[staff_id - 1]
    staff_db.pop(staff_id - 1)
    result = {'msg': f"{staff['name']} was delete!"}
    return result
