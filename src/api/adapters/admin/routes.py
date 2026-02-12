from os.path import basename, join

from fastapi import FastAPI, UploadFile
from sqladmin import Admin, ModelView
from sqladmin.filters import AllUniqueStringValuesFilter, OperationColumnFilter
from wtforms import FileField

from api.adapters.schemas.models import CategoryModel, FoodModel, FoodPhotoModel
from api.infra.db import engine
from api.infra.settings import MEDIA_DIR


def register_admin(app : FastAPI):
    admin = Admin(app , engine)

    class FoodAdmin(ModelView , model = FoodModel): #type: ignore
        column_list = [FoodModel.id , FoodModel.name , FoodModel.price]
        column_filters = [
            OperationColumnFilter(FoodModel.price)
        ]
        column_details_list = [*column_list , FoodModel.slug , FoodModel.categories ]
        column_formatters_detail = {FoodModel.categories : lambda model , column :model.categories}
        form_columns = ["name" , "description" , "price" , "photos" , "categories"]
        category = "Meal"
        name = "Food"
        name_plural = "Foods"
        icon = "fa-solid fa-bowl-food"
        category_icon = "fa-solid fa-bowl-food"
        column_searchable_list = [FoodModel.name]
        column_default_sort = [(FoodModel.name , False)]

        async def on_model_change(self, data, model, is_created, request):
            slug = data.get("name").lower().replace(" " , "-")
            model.slug = slug

            data["slug"] = model.slug


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
        form_columns = ["name" , "image"]

        async def on_model_change(self, data, model, is_created, request):
            slug = data.get("name").lower().replace(" " , "-")
            model.slug = slug

            data["slug"] = model.slug

    class FoodPhotoAdmin(ModelView , model=FoodPhotoModel): #type: ignore
        column_list = [FoodPhotoModel.id , FoodPhotoModel.food]
        name = "Food Photo"
        name_plural = "Foods Photos"
        icon = "fa-solid fa-image"
        category = "Meal"
        column_formatters = {FoodPhotoModel.food : lambda model , column : model.food.name }
        column_formatters_detail = {FoodPhotoModel.food : lambda model , column : model.food.name }
        column_details_exclude_list = [FoodPhotoModel.food_id]
        form_overrides = {
            "photo_url" : FileField
        }

        async def on_model_change(self, data, model, is_created, request):
            photo : UploadFile = data.get("photo_url") #type: ignore
            if photo:
                filename = basename(photo.filename)
                upload_path = join(MEDIA_DIR , filename)
                with open(upload_path , "wb") as buffer:
                    buffer.write(await photo.read())
                model.photo_url = filename

            data["photo_url"] = model.photo_url


    admin.add_view(FoodAdmin)
    admin.add_view(FoodPhotoAdmin)
    admin.add_view(CategoriesAdmin)
