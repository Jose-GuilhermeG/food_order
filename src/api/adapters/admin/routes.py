from fastapi import FastAPI
from sqladmin import Admin, ModelView
from sqladmin.filters import AllUniqueStringValuesFilter, OperationColumnFilter

from api.adapters.factories import FoodFactory
from api.adapters.mapping import FoodMapping
from api.adapters.schemas.models import CategoryModel, FoodModel, FoodPhotoModel
from api.infra.db import engine


def register_admin(app : FastAPI):
    admin = Admin(app , engine)

    class FoodAdmin(ModelView , model = FoodModel): #type: ignore
        column_list = [FoodModel.id , FoodModel.name , FoodModel.price]
        column_filters = [
            OperationColumnFilter(FoodModel.price)
        ]
        column_details_list = [*column_list , FoodModel.slug ]
        form_columns = ["name" , "description" , "price" , "photos"]
        category = "Meal"
        name = "Food"
        name_plural = "Foods"
        icon = "fa-solid fa-bowl-food"
        category_icon = "fa-solid fa-bowl-food"
        column_searchable_list = [FoodModel.name]
        column_default_sort = [(FoodModel.name , False)]

        async def on_model_change(self, data, model, is_created, request):
            factory = FoodFactory(ignore_attrs=["id"])
            mapping = FoodMapping(factory)
            if not is_created:
                return mapping.to_model(factory.reconstruct(**data))

            slug = data.get("name").lower().replace(" " , "-")
            model.slug = slug

            return model


    class CategoriesAdmin(ModelView , model=CategoryModel): #type: ignore
        column_list = [CategoryModel.id , CategoryModel.name , CategoryModel.slug]
        column_details_list = [*column_list , CategoryModel.image]
        column_filters = [
            AllUniqueStringValuesFilter(CategoryModel.name)
        ]
        category = "Meal"
        name = "Category"
        name_plural ="Categories"
        column_searchable_list = [CategoryModel.name]
        column_default_sort = [(CategoryModel.name , False)]


    class FoodPhotoAdmin(ModelView , model=FoodPhotoModel): #type: ignore
        column_list = [FoodPhotoModel.id , FoodPhotoModel.food]
        name = "Food Photo"
        name_plural = "Foods Photos"
        icon = "fa-solid fa-image"
        category = "Meal"
        column_formatters = {FoodPhotoModel.food : lambda model , column : model.food.name }
        column_formatters_detail = {FoodPhotoModel.food : lambda model , column : model.food.name }
        column_details_exclude_list = [FoodPhotoModel.food_id]

    admin.add_view(FoodAdmin)
    admin.add_view(FoodPhotoAdmin)
    admin.add_view(CategoriesAdmin)
