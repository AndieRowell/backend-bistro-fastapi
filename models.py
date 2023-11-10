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

    #need to put the connection/relationship to the other tables
        #does this need to have cuisine id mapped to the other table here instead of above?
        # - does it matter if out of order compared to sql
        # - am i still using a list?
    cuisine_id: Mapped[List["Cuisine"]] = relationship(back_populates="menu_item", cascade="all, delete-orphan")

    #also define the function to return the information using string interpolation
    #this code below autofilled in...
        # def __repr__(self) -> str:
        #     return super().__repr__()
    def __repr__(self) -> str:
        return f"Menu Item(id={self.id!r}, title={self.title!r}, cuisine={self.cuisine_id!r}, category={self.category_id!r}, description={self.description!r}, price={self.price!r}, spicy_level={self.spicy_level!r})"

# create another class for the cuisine table
class Cuisine(Base):


# create another class for the category table
