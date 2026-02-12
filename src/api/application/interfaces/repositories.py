from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from api.application.interfaces.mapping import IMapping
from api.domain.entities import Category, Food, Order, OrderIdentify

T = TypeVar("T")

class IAddOperation(
    ABC,
    Generic[T]
):
    @abstractmethod
    def save(self , entitie : T) -> T:
        pass

    @abstractmethod
    def create(self , entitie : T) -> T:
        pass

    @abstractmethod
    def create_group(self , list_entitie : list[T]) -> list[T]:
        pass


class IIdOperations(
    ABC,
    Generic[T]
):
    @abstractmethod
    def get_by_id(self , id : int)-> T | None:
        pass

    @abstractmethod
    def delete_by_id(self , id : int)->None:
        pass

class IReadOperation(
    ABC,
    Generic[T]
):
    @abstractmethod
    def all(self) -> list[T]:
        pass

    @abstractmethod
    def limit(self , limit : int , offeset : int) -> list[T]:
        pass



class IBaseRepository(
    IAddOperation[T],
    IReadOperation[T],
    Generic[T]
):
    def __init__(self , mapper : IMapping):
        self.mapper = mapper


class IRepository(
    IBaseRepository[T],
    IIdOperations[T],
    Generic[T]
):
    pass

class IFoodRepository(
    IRepository[Food],
):
    @abstractmethod
    def get_by_slug(self , slug : str)-> Food:
        pass

    @abstractmethod
    def search(self , q : str , category_slug : str)-> list[Food]:
        pass

    @abstractmethod
    def get_by_id_in_list(self, id_list : list[int]):
        pass

class ICategoryRepository(
    IRepository[Category]
):
    @abstractmethod
    def get_by_slug(self , slug : str)-> Category:
        pass

    @abstractmethod
    def exist_by_slug(self , slug : str)->bool:
        pass

class IOrderRepository(
    IBaseRepository[Order],
):
    pass
    #@abstractmethod
    #def get_orders_by_order_identify(self , order_identify : int)-> list[Order]:
    #    pass

class IOrderIdentifyRepository(
    IBaseRepository[OrderIdentify],
):
    @abstractmethod
    def get_last(self)->OrderIdentify:
        pass

    @abstractmethod
    def set_current_order_as_ready(self)->None:
        pass

    @abstractmethod
    def get_last_ready(self)->OrderIdentify:
        pass

    @abstractmethod
    def get_all(self)->list[OrderIdentify]:
        pass
