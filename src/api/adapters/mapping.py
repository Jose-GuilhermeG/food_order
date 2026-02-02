from typing import Generic, Type, TypeVar

from sqlmodel import SQLModel

from api.adapters.schemas.models import CategoryModel, FoodModel
from api.application.interfaces.mapping import IMapping
from api.domain.entities import Category, Food

T = TypeVar("T")
M = TypeVar("M")

class BaseMapping(
    IMapping,
    Generic[T , M],
):
    _entity : Type[T]
    _model : Type[M]

    def __init__(self, factory):
        super().__init__(factory)
        self._atrrs = [atrr for atrr in dir(self._entity) if not atrr.startswith("__") and not atrr.endswith("__") ]

    def to_entitie(self, model : SQLModel | list[SQLModel])-> T | list[T]:
        if isinstance(model , (list , tuple , set)):
            return self.to_entitie_many(model) #type: ignore

        return self._factory.reconstruct(**model.model_dump())

    def to_entitie_many(self , models : list[SQLModel]) -> list[T]:
        entity_list = []
        for model in models:
            entity_list.append(self._factory.reconstruct(**model.model_dump()))

        return entity_list

    def to_model(self, entity : T | list[T]) -> M | list[M]:
        if isinstance(entity , (list , tuple , set)):
            return self.to_model_many(entity)

        model_data = self.get_class_attrs(entity)
        return self._model(**model_data)

    def to_model_many(self , entities) -> list[M] :
        models_list = []
        for entity in entities:
            model_data = self.get_class_attrs(entity)
            models_list.append(self._model(**model_data))

        return models_list

    def get_class_attrs(self , cls):
        data = {}
        for attr in self._atrrs:
            data[attr] = getattr(cls , attr)
        return data


class FoodMapping(
    BaseMapping[Food , FoodModel],
):
    _entity = Food
    _model = FoodModel

class CategoryMapping(
    BaseMapping[Category , CategoryModel]
):

    _entity = Category
    _model = CategoryModel
