from typing import Generic, Type, TypeVar

from sqlmodel import SQLModel

from api.adapters.schemas.models import CategoryModel, FoodModel, FoodPhotoModel
from api.application.interfaces.mapping import IMapping
from api.domain.entities import Category, Food, FoodPhoto

T = TypeVar("T")
M = TypeVar("M")

class BaseMapping(
    IMapping,
    Generic[T , M],
):
    _entity : Type[T]
    _model : Type[M]
    _attrs : list[str] = []
    _extra_mappings : dict[str , IMapping] = {}

    def __init__(self, factory ,  extra_mappings : dict[str , IMapping] = {}):
        super().__init__(factory)
        self._extra_mappings = extra_mappings
        if len(self._attrs) == 0:
            self._attrs = [
                atrr.replace("__","").replace(self._entity.__name__ , "").removeprefix('_')
                for atrr in self._entity.__annotations__ if atrr.startswith(f"_{self._entity.__name__}__") and not atrr.endswith("__")
            ]

    def get_values(self , cls , is_model : bool = False):
        data = {}
        for attr in self._attrs:
            data[attr] = self.get_data_mapping(cls , attr , is_model)
        return data

    def get_data_mapping(self , cls , attr , is_model : bool = False):
        mapping = self._extra_mappings.get(attr, None)
        data_not_mapping = getattr(cls,attr)
        if not mapping :
            return data_not_mapping
        if is_model:
            return mapping.to_entitie(data_not_mapping)

        return mapping.to_model(data_not_mapping)

    def to_entitie(self, model : SQLModel | list[SQLModel])-> T | list[T]:
        if isinstance(model , (list , tuple , set)):
            return self.to_entitie_many(model) #type: ignore
        return self._factory.reconstruct(**self.get_values(model , is_model=True))

    def to_entitie_many(self , models : list[SQLModel]) -> list[T]:
        entity_list = []
        for model in models:
            entity_list.append(self._factory.reconstruct(**self.get_values(model , is_model=True)))

        return entity_list

    def to_model(self, entity : T | list[T]) -> M | list[M]:
        if isinstance(entity , (list , tuple , set)):
            return self.to_model_many(entity)

        model_data = self.get_values(entity)
        return self._model(**model_data)

    def to_model_many(self , entities) -> list[M] :
        models_list = []
        for entity in entities:
            model_data = self.get_values(entity)
            models_list.append(self._model(**model_data))

        return models_list



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

class FoodPhotoMapping(
    BaseMapping[FoodPhoto , FoodPhotoModel],
):
    _entity = FoodPhoto
    _model = FoodPhotoModel
