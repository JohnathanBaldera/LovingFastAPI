from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
import bcrypt
from data.user_data import user_data # pylint: disable=E0401


app = FastAPI()

# Example of Users API Endpoint

# A Base Class that defines what we expect in every User Model


class UserBase(BaseModel):
    username: str
    email: EmailStr
    name: str

# New Users create a password.  We NEVER respond with a request sending their password
# Passwords should not be stored in databases, hashed values should be stored instead
# This example is meant to be concise but not standard practice of authentication


class UserIn(UserBase):
    password: str

# Once a User is in our database, they will have unique ID generated and assigned that we expose


class UserOut(UserBase):
    id: int


class UserInDB(UserOut):
    hashed_pw: str

# response_model parameter will filter out our return JSON to match the given type


@app.get("/users", response_model=List[UserOut])
async def get_users():
    return user_data


@app.post("/users", response_model=UserOut)
async def create_user(user: UserIn):
    new_id = len(user_data) + 1
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(bytes(user.password, 'utf-8'), salt)
    new_user = UserInDB(**user.dict(), hashed_pw=hashed, id=new_id)
    user_data.append(new_user)
    return user_data[new_id - 1]


@app.get("/users/{user_id}", response_model=UserOut)
async def get_user(user_id: int):
    return user_data[user_id]
