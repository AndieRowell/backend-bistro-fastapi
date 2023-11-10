from typing import List
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table

class Base(DeclarativeBase):
    pass

class Menu_item(Base):
    __tablename__ = "menu_item"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = Column(String, default="Title")
    cuisine_id: Mapped[int] = Column(Integer, default="Cuisine Type")
    category_id: Mapped[int] = Column(Integer, default="Category Type")
    description: Mapped[str] = Column(String, default="Description")
    price: Mapped[int] = Column(Integer, default="Price")
    spicy_level: Mapped[int] = Column(Integer, default="Spiciness Level")

    #need to put the connection/relationship to the othe tables



    #also define the function to return the information using string interpolation

# create another class for the cuisine table

# create another class for the category table
