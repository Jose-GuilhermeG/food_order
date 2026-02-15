from sqlalchemy import Column, Numeric, Text
from sqlmodel import Field, Relationship, SQLModel


class BaseModel(
    SQLModel,
):
    id : int | None = Field(default=None , primary_key=True , unique=True)

class FoodCategoryModel(
    BaseModel,
    table = True #type: ignore[call-arg]
):
    food_id : int = Field(foreign_key="food.id")
    category_id : int = Field(foreign_key="category.id")


class FoodModel(
    BaseModel,
    table = True #type: ignore[call-arg]
):
    __tablename__ = "food"

    name : str = Field(
        title="Nome do alimento",
        max_length=120 ,
        index=True
    )
    slug : str = Field(
        title="slug do alimento",
        max_length=120 ,
        unique=True
    )
    description : str | None = Field(
        title="Descrição do alimento",
        default="" ,
        max_length=255
    )
    price : float = Field(
        title="Preço do alimento",
        max_digits=10,
        decimal_places=2,
        sa_column=Column(
            Numeric(10,2)
        ),
        ge=1
    )
    categories : list["CategoryModel"] = Relationship(
        back_populates="foods",
        link_model=FoodCategoryModel
    )
    photos : list["FoodPhotoModel"] = Relationship(
        back_populates="food"
    )

class CategoryModel(
    BaseModel,
    table = True #type: ignore[call-arg]
):
    __tablename__ = "category"

    name : str = Field(
        title="Nome da categoria",
        max_length=90,
        unique=True
    )
    image : str = Field(
        title="Imagem da categoria",
        default="",
        sa_column=Column(Text)
    )
    slug : str = Field(
        title="Slug da categoria",
        max_length=90,
        unique = True
    )

    foods : list["FoodModel"] = Relationship(
        back_populates="categories",
        link_model=FoodCategoryModel
    )

class FoodPhotoModel(
    BaseModel,
    table = True #type: ignore[call-arg]
):
    food_id : int = Field(foreign_key="food.id")
    photo_url : str = Field(
        title="Url da foto ddo alimento",
        sa_column=Column(Text)
    )
    food: "FoodModel" = Relationship(back_populates="photos")
