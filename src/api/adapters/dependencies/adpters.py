from typing import Annotated

from fastapi import Depends

from api.adapters.dependencies.db import SessionDep
from api.adapters.factories import CategoryFactory, FoodFactory, FoodPhotoFactory
from api.adapters.mapping import CategoryMapping, FoodMapping, FoodPhotoMapping
from api.adapters.repository import CategoryRepositoryDb, FoodRepositoryDb
from api.application.interfaces.factories import (
    ICategoryFactory,
    IFactory,
    IFoodFactory,
)
from api.application.interfaces.mapping import IMapping
from api.application.interfaces.repositories import ICategoryRepository, IFoodRepository


def get_food_photo_factory()->IFactory:
    return FoodPhotoFactory()

FoodPhotoFactoryDep = Annotated[IFactory , Depends(get_food_photo_factory)]

def get_food_photo_mapping(get_food_photo_factory : FoodPhotoFactoryDep):
    return FoodPhotoMapping(get_food_photo_factory)

FoodPhotoMappingDep = Annotated[IMapping , Depends(get_food_photo_mapping)]

def get_food_factory()->IFoodFactory:
    return FoodFactory()

FoodFactoryDep = Annotated[IFoodFactory , Depends(get_food_factory)]

def get_food_mapping(food_factory : FoodFactoryDep , food_photo_mapping : FoodPhotoMappingDep)->IMapping:
    return FoodMapping(food_factory , extra_mappings={'photos' : food_photo_mapping})

FoodMappingDep = Annotated[IMapping , Depends(get_food_mapping)]

def get_food_repository(food_mapping : FoodMappingDep , session : SessionDep) -> IFoodRepository:
    return FoodRepositoryDb(food_mapping,session)

FoodRepositoryDep = Annotated[IFoodRepository , Depends(get_food_repository)]

def get_category_factory()->ICategoryFactory:
    return CategoryFactory()

CategoryFactoryDep = Annotated[ICategoryFactory , Depends(get_category_factory)]

def get_category_mapping(category_factory : CategoryFactoryDep)->IMapping:
    return CategoryMapping(category_factory)

CategoryMappingDep = Annotated[IMapping , Depends(get_category_mapping)]

def get_category_repository(category_mapping : CategoryMappingDep , session : SessionDep) -> ICategoryRepository:
    return CategoryRepositoryDb(category_mapping,session)

CategoryRepositoryDep = Annotated[ICategoryRepository , Depends(get_category_repository)]
