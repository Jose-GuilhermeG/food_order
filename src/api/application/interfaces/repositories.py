from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from api.application.interfaces.mapping import IMapping

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
    def get_by_id(self , field : str , id : int , exec : bool = True)-> T | None:
        pass

    @abstractmethod
    def all(self , exec : bool = True)-> list[T]:
        pass

    @abstractmethod
    def limit(self , limit : int , offeset : int ,exec : bool = True) -> list[T]:
        pass

    @abstractmethod
    def delete_by_id(self , id : int)->None:
        pass
