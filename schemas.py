from typing import Optional
from pydantic import BaseModel

class CategoryModel(BaseModel):
    id: int
    category_type: str | None

class CuisineModel(BaseModel):
    id: int
    cuisine_type: str | None

class MenuItemModel(BaseModel)
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
