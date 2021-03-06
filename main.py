from fastapi import FastAPI 
from tortoise.contrib.fastapi import register_tortoise
from models.todo import Todos, Todos_Pydantic, TodosIn_Pydantic


app = FastAPI()


@app.get("/")
def route():
    return {'msg': 'well come FastAPI todo list'}


@app.get('/todos')
async def show_all_todos():
    return await Todos_Pydantic.from_queryset(Todos.all())


@app.get('/todo/{todo_id}')
async def todo_by_id(todo_id: int):
    return await Todos_Pydantic.from_queryset_single(Todos.get(id=todo_id))


@app.post('/todo')
async def create_todo(todo: TodosIn_Pydantic):
    todo_obj = await Todos.create(**todo.dict(exclude_unset=True))
    return await TodosIn_Pydantic.from_tortoise_orm(todo_obj)


@app.put('/todo/{todo_id}')
async def update_todo(todo_id:int, todo: TodosIn_Pydantic):
    await Todos.filter(id=todo_id).update(**todo.dict(exclude_unset=True))
    return await Todos_Pydantic.from_queryset_single(Todos.get(id=todo_id))


@app.delete('/todo/{todo_id}')
async def delete_todo(todo_id: int):
    todo_count = await Todos.filter(id=todo_id).delete()
    if not todo_count:
        return {'msg': f"Todo {todo_id} not found!"}
    return {'msg': f"Todo {todo_id} delete successfull!"}


register_tortoise(
    app,
    db_url='sqlite://db.sqlite2',
    modules={'models': ['main']},
    generate_schemas=True,
    add_exception_handlers=True
)