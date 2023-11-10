from fastapi import FastAPI #import fastapi
from typing import List
#need to import models created from models.py file

#need to import sqlalchemy

#need to import routes? - need clarification on routes and router



app = FastAPI() #creates an api object - initializes it - always need to have this
#previous project also had "app.include_router(heroes.router)"
    #figure out what this does exactly - how does this connect?


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get
