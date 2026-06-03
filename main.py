# IMPORTACOES
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services import user_repository
import sqlite3

# CLASSE DE MODELO DE USUÁRIO
class User(BaseModel):
    name: str
    email: str

# INSTANCIACAO DE FASTAPI
app = FastAPI()

# ROTAS
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/users")
def read_users():
    users = user_repository.get_users()
    return {"users": users}

@app.post("/users")
def create_user(user: User):
    try:
        user_repository.create_user(
            name=user.name,
            email=user.email
        )

        return {
            "message": "User created successfully!"
        }

    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Email already exists.")

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return user_repository.update_user(
        user_id=user_id,
        name=user.name,
        email=user.email
    )

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return user_repository.delete_user(user_id)
