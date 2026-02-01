from typing import Annotated

from fastapi import Depends

from api.adapters.dependencies.db import SessionDep
from api.adapters.factories import FoodFactory
from api.adapters.mapping import FoodMapping
from api.adapters.repository import FoodRepositoryDb
from api.application.interfaces.factories import IFoodFactory
from api.application.interfaces.mapping import IMapping
from api.application.interfaces.repositories import IFoodRepository


def get_food_factory()->IFoodFactory:
    return FoodFactory()

FoodFactoryDep = Annotated[IFoodFactory , Depends(get_food_factory)]

def get_food_mapping(food_factory : FoodFactoryDep)->IMapping:
    return FoodMapping(food_factory)

FoodMappingDep = Annotated[IMapping , Depends(get_food_mapping)]

def get_food_repository(food_mapping : FoodMappingDep , session : SessionDep) -> IFoodRepository:
    return FoodRepositoryDb(food_mapping,session)

FoodRepositoryDep = Annotated[IFoodRepository , Depends(get_food_repository)]
