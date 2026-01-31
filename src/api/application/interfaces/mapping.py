from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from api.application.interfaces.factories import IFactory
from api.domain.entities import Category, Food, Order, OrderIdentify

T = TypeVar("T")
M = TypeVar("M")

class IMapping(ABC, Generic[T, M]):
    def __init__(self, factory: IFactory[T]) -> None:
        self._factory = factory

    @abstractmethod
    def to_model(self, entity: T) -> M:
        pass

    @abstractmethod
    def to_entitie(self, model: M) -> T:
        pass

class ICategoryMapping(IMapping[Category, M], ABC):
    pass


class IFoodMapping(IMapping[Food, M], ABC):
    pass


class IOrderMapping(IMapping[Order, M], ABC):
    pass


class IOrderIdentifyMapping(IMapping[OrderIdentify, M], ABC):
    pass
