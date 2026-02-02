from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from api.application.interfaces.mapping import IMapping
from api.domain.entities import Category, Food

T = TypeVar("T")

class IRepository(
    ABC,
    Generic[T]
):
    def __init__(self , mapper : IMapping):
        self.mapper = mapper

    @abstractmethod
    def save(self , entitie : T) -> T:
        pass

    @abstractmethod
    def create(self , entitie : T) -> T:
        pass

    @abstractmethod
    def get_by_id(self , id : int)-> T | None:
        pass

    @abstractmethod
    def all(self) -> list[T]:
        pass

    @abstractmethod
    def limit(self , limit : int , offeset : int) -> list[T]:
        pass

    @abstractmethod
    def delete_by_id(self , id : int)->None:
        pass


class IFoodRepository(
    IRepository[Food],
):
    pass

class ICategoryRepository(
    IRepository[Category]
):
    pass
