from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Victor", surname="Del Rio", url="https://victordev.super.site/", age=29),
              User(id=2, name="Del Rio", surname="Victor", url="https://delriodev.super.site/", age=33),
              User(id=3, name="Daniel", surname="Leon", url="https://danieldev.super.site/", age=35)]

app = FastAPI()

@app.get("/users")
async def users():
    return users_list

#path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#query
@app.get("/user/")
async def user(id: int):
    return search_user(id)

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error": "No se ha encontrado el usuario"}
