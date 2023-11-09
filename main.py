from fastapi import FastAPI #import fastapi
from typing import List

app = FastAPI() #creates an api object - initializes it - always need to have this


@app.get("/")
async def root():
    return {"message": "Hello World"}

