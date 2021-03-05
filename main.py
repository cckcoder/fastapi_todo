from fastapi import FastAPI

from views import coffees, staff


app = FastAPI()


@app.get("/")
def route():
    return {'msg': 'well come Python Coffee shop'}


def config_router():
    app.include_router(coffees.router)
    app.include_router(staff.router)

config_router()