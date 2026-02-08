from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from api.domain.entities import Category, Food, Order, OrderIdentify

T = TypeVar("T")

class IFactory(
    ABC,
    Generic[T]
):
    _ignore_attrs : list[str] = []

    @abstractmethod
    def create(self , **kwargs) -> T: pass

    @abstractmethod
    def reconstruct(self , **kwrags) -> T : pass

class ICategoryFactory(IFactory[Category], ABC):
    pass

class IFoodFactory(IFactory[Food], ABC):
    pass

class IOrderFactory(IFactory[Order], ABC):
    pass

class IOrderIdentifyFactory(IFactory[OrderIdentify], ABC):
    pass
