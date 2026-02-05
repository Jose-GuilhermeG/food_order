from typing import Generic, Type, TypeVar

from api.application.interfaces.factories import (
    ICategoryFactory,
    IFactory,
    IFoodFactory,
)
from api.domain.entities import Category, Food, FoodPhoto

T = TypeVar("T")

class BaseFactory(
    IFactory,
    Generic[T]
):
    _model : Type[T]
    _private_attrs : list[str] = []
    _public_attrs : list[str] = []
    _ignore_attrs : list[str] = []

    def __init__(self , ignore_attrs  : list[str] = []):
        self._public_attrs = [atrr for atrr in dir(self._model) if not atrr.startswith("__") and not atrr.endswith("__") and atrr not in self._ignore_attrs ]
        self._private_attrs = [atrr for atrr in self._model.__annotations__ if atrr.startswith(f"_{self._model.__name__}__") and not atrr.endswith("__")]
        self._ignore_attrs = ignore_attrs

    def create(self, **kwargs):
        instance = self._model()
        for atrr in self._public_attrs:
            setattr(instance , atrr , kwargs.get(atrr))

        return instance

    def reconstruct(self, **kwargs):
        instance = self._model()
        for atrr in self._private_attrs:
            format_attr_name = atrr.replace("__" , "").replace(self._model.__name__ , "").removeprefix('_')
            setattr(instance , atrr , kwargs.get(format_attr_name))

        return instance


class FoodFactory(
    BaseFactory[Food],
    IFoodFactory,
) :
    _model = Food

class CategoryFactory(
    BaseFactory[Category],
    ICategoryFactory
):
    _model = Category

class FoodPhotoFactory(
    BaseFactory[FoodPhoto],
):
    _model = FoodPhoto
