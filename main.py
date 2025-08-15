from fastapi import FastAPI, Request
from db import users_collection
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "API is working"}

class RegisterInput(BaseModel):
    email: str

@app.post("/register")
def register_user(payload: RegisterInput):
    users_collection.insert_one({"email": payload.email})
    return {"status": "User registered"}
