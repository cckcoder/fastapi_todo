from fastapi import APIRouter 
from tortoise.contrib.fastapi import register_tortoise
from models.todo_list import Todo, Todo_Pydantic, TodoIn_Pydantic
from ..main import app

router = APIRouter(
    prefix="/todo",
    tags=['Todo'],
    responses={404: {'message': "Not found"}}
)

@router.post('todo')
async def create_todo(todo: TodoIn_Pydantic):
    todo_obj = await Todo.create(**todo.dict(exclude_unset=True))
    return await Todo_Pydantic.from_tortoise_orm(todo_obj)


register_tortoise(
    app,
    db_url='sqlite://db.sqlite2',
    modules={'models': ['main']},
    generate_schemas=True,
    add_exception_handlers=True
)
