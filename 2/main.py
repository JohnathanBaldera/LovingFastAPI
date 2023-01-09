from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# This accepts a path parameter {num} without type hints
# Path parameters are identified when they are part
# of the decorator and function.
@app.get("/nohint/{num}")
async def return_string(num):
    return num

# This accepts a path parameter {num} with type hints.
# This allows for validation on upon recieving the request and
# auto conversion of type with its response
@app.get("/hint/{num}")
async def return_num(num: int):
    return num


# This accepts query parameters {number} and {string}
# Without type hints, our linter will not be able to catch unsupported operations between types
# Query parameters are identified when they are passed only to the function
# and represent a singular type (int, float, str, bool, etc...)
@app.get('/hide')
async def hide_error(number, string):
    return string / number

# Due to our type hints, our linter can catch that dividing a str and int is not a valid operation
# This helps to catch errors before runtime
@app.get('/show')
async def show_error(string: str, number: Optional[int] = None):
    return string / number
