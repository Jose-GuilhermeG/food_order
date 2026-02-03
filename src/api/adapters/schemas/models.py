from sqlalchemy import Column, Text
from sqlmodel import Field, Relationship, SQLModel


class BaseModel(
    SQLModel,
):
    id : int | None = Field(default=None , primary_key=True , unique=True)

class FoodCategoryModel(
    BaseModel,
    table = True #type: ignore[call-arg]
):
    food_id : int = Field(foreign_key="foodmodel.id")
    category_id : int = Field(foreign_key="categorymodel.id")


class FoodModel(
    BaseModel,
    table = True #type: ignore[call-arg]
):
    name : str
    slug : str
    description : str
    price : float
    categories : list["CategoryModel"] = Relationship(
        back_populates="foods",
        link_model=FoodCategoryModel
    )

class CategoryModel(
    BaseModel,
    table = True #type: ignore[call-arg]
):
    name : str = Field(unique=True)
    image : str = Field(sa_column=Column(Text))
    slug : str = Field(unique = True)

    foods : list["FoodModel"] = Relationship(
        back_populates="categories",
        link_model=FoodCategoryModel
    )
