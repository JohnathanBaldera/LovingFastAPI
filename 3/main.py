from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import bcrypt
from .user_data import user_data


app = FastAPI()

# Example of Users API Endpoint

# A Base Class that defines what we expect in every User Model


class UserBase(BaseModel):
    username: str
    email: EmailStr

# New Users create a password.  We NEVER respond with a request sending their password
# Passwords should not be stored in databases, hashed values should be stored instead


class UserIn(UserBase):
    password: str

# Once a User is in our database, they will have unique ID generated and assigned that we expose


class UserOut(UserBase):
    id: int

# response_model parameter will filter out our return JSON to match the given type


@app.get("/users", response_model=List[UserOut])
async def get_users():
    return user_data


@app.post("/users", response_model=UserOut)
async def new_user(user: UserIn):
    new_id = len(user_data) + 1
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(user.password, salt)
    user["hashed_pw"] = hashed
    user["id"] = new_id
    return user_data[new_id]


@app.get("/users/{user_id}", response_model=UserOut)
async def get_user(user_id: int):
    return user_data[user_id]
