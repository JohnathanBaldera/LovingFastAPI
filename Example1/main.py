# Example of how simple and fast you can build with FastAPI
# Auto Documentation is built in from the beginning
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Python Austin!"}
