from sqlalchemy import Column, Text
from sqlmodel import Field, SQLModel


class BaseModel(
    SQLModel,
):
    id : int | None = Field(default=None , primary_key=True , unique=True)

class FoodModel(
    BaseModel,
    table = True #type: ignore[call-arg]
):
    name : str
    slug : str
    description : str
    price : float

class CategoryModel(
    BaseModel,
    table = True #type: ignore[call-arg]
):
    name : str = Field(unique=True)
    image : str = Field(sa_column=Column(Text))
    slug : str = Field(unique = True)
