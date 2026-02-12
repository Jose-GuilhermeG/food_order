from typing import Annotated

from fastapi import APIRouter, Path

from api.adapters.dependencies.adpters import CategoryRepositoryDep, FoodRepositoryDep
from api.adapters.schemas.schemas import FoodListSerializer, FoodSerializer
from api.application.use_cases.food_use_cases import (
    FoodDetailUseCase,
    ListFoodUseCase,
    SearchFoodUseCase,
)

router = APIRouter(
    prefix='/food',
    tags=['food']
)

@router.get(
    '/',
    response_model=list[FoodListSerializer]
)
def list_food_view(food_repository : FoodRepositoryDep):
    result = ListFoodUseCase(food_repository).execute()
    return [ FoodListSerializer.to_schema(food) for food in result ]

@router.get(
    '/{slug}/',
    response_model=FoodSerializer
)
async def detail_food_view(slug : str , food_repository : FoodRepositoryDep):
    result = FoodDetailUseCase(food_repository).execute(slug)
    return FoodSerializer.to_schema(result)

@router.get(
    "/search/{search}/{slug}/",
    response_model=list[FoodListSerializer]
)
def search_food_view(search : str , slug : Annotated[str , Path()]  , repository : FoodRepositoryDep , category_repository : CategoryRepositoryDep):
    result = SearchFoodUseCase(repository , category_repository).execute(search , slug)
    return [FoodListSerializer.to_schema(food) for food in result]
