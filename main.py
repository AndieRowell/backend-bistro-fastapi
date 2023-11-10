from fastapi import FastAPI, Depends, HTTPException #import fastapi
from typing import List
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models import Category, Cuisine, Menu_item
from pydantic import BaseModel
from schemas import CategoryModel, CuisineSchema, MenuItemsSchema # i think i need to change these to mine
#need to import models created from models.py file

#need to import sqlalchemy

#need to import routes? - need clarification on routes and router


app = FastAPI() #creates an api object - initializes it - always need to have this
#previous project also had "app.include_router(heroes.router)"
    #figure out what this does exactly - how does this connect?


@app.get("/") #/ is our path/endpoint
async def root():
    return {"message": "Hello World"} #this is the information we will see at this specific endpoint

#trying to understand how to create a route - and connecting to classes and using path parameters
# @app.get("/menu_item")
# async def menu_item(#what am i placing in here? the full menu layout?)
#     return #return the full menu string interpolation?

@app.get("/menu_item")
def get_menu_item(db: Session = Depends(get_db)):
    result = db.query(Menu_item, Cuisine, Category).join(Cuisine, Menu_item.cuisine_id == Cuisine.id).join(Category, Menu_item.category_id == Category.id)
    pydantic_result = []


#need to create the path - and connect the query
#create a for loop to go thrrough and show the menu items

    for menu_item, cuisine, category in result:
        category_schema = CategorySchema(id=category.id, category_type=category.category_type)
        cuisine_schema = CuisineSchema(id-cuisine.id, cuisine_type=cuisine.cuisine_type)

    menu_item_schema = MenuItemsSchema(
        id=menu_item.id,
        title=menu_item.title,
        cuisine=cuisine_schema
        category=category_schema
        description=menu_item.description
        price=menu_item.price
        spicy_level=menu_item.spicy_level
    )

    pydantic_result.append(menu_item_schema)

return pydantic_result
