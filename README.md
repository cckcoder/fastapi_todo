# Introduct FastAPI

## Hello World

### Setup tools and env

- Create virtual env

```
python3 -m venv env
```

- Activate vertual env

```
source env/bin/activate
```

- Install FastAPI

```
pip install fastapi
```

- Install hypercorn

```
pip install hypercorn
```

## Create main.py

```python
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hello_world():
    return {'hello': 'world'}
```

## Swagger UI

- Swagger UI ทำให้เราสามารถจัดการ ในส่วน route api ได้อย่างง่ายดาย
  - เช่น เราสามารถ ดูผลลัพธ์ จากหน้านี้ได้เลย เหมือนมี Post Man Buil-in มาเลยครับ
  - ลองดูกันเลยครับ `localhost:8000/docs`
