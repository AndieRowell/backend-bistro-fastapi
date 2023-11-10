from typing import Optional
from pydantic import BaseModel

class CategorySchema(BaseModel):
    id: int
    category_type: str | None

class CuisineSchema(BaseModel):
    id: int
    cuisine_type: str | None

class MenuItemSchema(BaseModel)
    id: int
    title: str | None
    cuisine_id: int
    category_id: int
    description: str | None
    price: int
    spicy_level: int

def __init__(self,**data):
    super().__init__(**data)

class Config:
    from_attributes = True
