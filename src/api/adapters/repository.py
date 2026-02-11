from typing import Any, Type, TypeVar

from sqlalchemy.orm import selectinload
from sqlmodel import Session, SQLModel, delete, select

from api.adapters.queue import OrderQueue
from api.adapters.schemas.models import CategoryModel, FoodModel
from api.application.interfaces.repositories import (
    ICategoryRepository,
    IFoodRepository,
    IOrderIdentifyRepository,
    IRepository,
)
from api.domain.entities import Category, Food
from api.domain.exceptions import IntegrityException

T = TypeVar("T" , bound=SQLModel)

class RepositoryDb(
    IRepository[T],
):
    _model : Type[T] = None #type: ignore
    _extra_models : Any

    def __init__(self, mapper  , session : Session):
        super().__init__(mapper)
        self.session = session

    def get_by_id(self, id, exec = True):
        query = self.session.get(self._model , id)
        if exec:
            return self.mapper.to_entitie(self.exec(query))

        return query

    def all(self, exec = True) -> list[T]:
        query = select(self._model)
        if exec:
            return self.mapper.to_entitie(self.exec(query).all())

        return query

    def limit(self, limit, offeset , exec = True):
        query = select(self._model).limit(limit).offset(offeset)
        if exec:
            return self.mapper.to_entitie(self.exec(query).all())
        return query

    def create(self, entitie):
        model = self.mapper.to_model(entitie)
        self.session.add(model)
        self.session.flush()
        return self.mapper.to_entitie(model)

    def create_group(self, list_entitie):
        models_list = self.mapper.to_model(list_entitie)
        self.session.add_all(models_list)
        self.session.flush()
        return self.mapper.to_entitie(models_list)

    def save(self, entitie):
        model = self.mapper.to_model(entitie)
        self.session.merge(model)
        return self.mapper.to_entitie(model)

    def delete_by_id(self, id):
        statement = delete(self._model).where(self._model.id == id)
        self.exec(statement)
        self.session.flush()

    def exec(self,query):
        return self.session.exec(query)

    def _select(self , *data):
        query = select(*data).options(
            selectinload(
                *self._extra_models
            )
        )

        return query

class FoodRepositoryDb(
    RepositoryDb[Food],
    IFoodRepository,
):
    _model = FoodModel
    _extra_models = [FoodModel.photos]

    def get_by_slug(self, slug , exec : bool = True):
        query = self._select(self._model).where(self._model.slug == slug)

        if not exec:
            return query

        query_result = self.exec(query).first()

        if query_result is None:
            raise IntegrityException("food not found")

        return self.mapper.to_entitie(query_result)

    def search(self, q , exec : bool = True):
        query = select(self._model).where(self._model.name.ilike(f"%{q}%")) #type: ignore

        if exec:
            return self.mapper.to_entitie(self.exec(query).all())

        return query

    def get_by_id_in_list(self, id_list , exec : bool = True):
        query = select(self._model).where(self._model.id.in_(id_list)) #type: ignore

        if exec:
            return self.mapper.to_entitie(self.exec(query).all())

        return query


class CategoryRepositoryDb(
    RepositoryDb[Category],
    ICategoryRepository
):
    _model = CategoryModel
    _extra_models = [CategoryModel.foods]

    def get_by_slug(self, slug , exec : bool = True):
        query = select(self._model).options(selectinload(self._model.foods)).where(self._model.slug == slug)

        if not exec:
            return query

        query_result = self.exec(query).first()

        if query_result is None:
            raise IntegrityException("Category not found")

        return self.mapper.to_entitie(query_result)

class OrderIdentifyRepository(
    IOrderIdentifyRepository
):
    def __init__(self , queue : OrderQueue )->None:
        self._queue = queue

    def create(self, entitie):
        return self._queue.add(entitie)

    def save(self, entitie):
        return entitie

    def all(self):
        return self._queue.all()

    def limit(self, limit, offeset):
        return []

    def get_last(self):
        return self._queue.get_last()

    def create_group(self, list_entitie):
        return []

    def set_current_order_as_ready(self):
        return self._queue.set_current_order_ready()

    def get_last_ready(self):
        return self._queue.get_ready_order()

    def get_all(self):
        return self._queue.all()
