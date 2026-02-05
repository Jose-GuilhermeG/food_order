from fastapi import FastAPI
from sqladmin import Admin, ModelView
from sqladmin.filters import AllUniqueStringValuesFilter

from api.adapters.factories import FoodFactory
from api.adapters.mapping import FoodMapping
from api.adapters.schemas.models import CategoryModel, FoodModel
from api.infra.db import engine


def register_admin(app : FastAPI):
    admin = Admin(app , engine)

    class FoodAdmin(ModelView , model = FoodModel): #type: ignore
        column_list = [FoodModel.id , FoodModel.name , FoodModel.slug , FoodModel.price]
        column_filters = [
            AllUniqueStringValuesFilter(FoodModel.name)
        ]
        column_details_list = [*column_list]
        form_columns = ["name" , "description" , "price" , "photos"]


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

    admin.add_view(FoodAdmin)
    admin.add_view(CategoriesAdmin)
