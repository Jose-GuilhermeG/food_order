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
async def list_food_view(food_repository : FoodRepositoryDep):
    """
        # List food route
        Get all foods registrated in database
    """
    result = ListFoodUseCase(food_repository).execute()
    return [ FoodListSerializer.to_schema(food) for food in result ]

@router.get(
    '/{slug}/',
    response_model=FoodSerializer
)
async def detail_food_view(slug : str , food_repository : FoodRepositoryDep):
    """
        # Food detail route
        Get food by slug

        ## Args:
        - **slug**: a simple str what repr the meal
    """
    result = FoodDetailUseCase(food_repository).execute(slug)
    return FoodSerializer.to_schema(result)

@router.get(
    "/search/{search}/{category_slug}/",
    response_model=list[FoodListSerializer]
)
async def search_food_view(search : str , category_slug : Annotated[str , Path()]  , food_repository : FoodRepositoryDep , category_repository : CategoryRepositoryDep):
    """
        # Food search route
        Get foods what name include the search str and has same category slug than category_slug

        ## Args
        - **category_slug** :  a simple str what repr the category
        - **search** : the str used to search foods
    """
    result = SearchFoodUseCase(food_repository , category_repository).execute(search , category_slug)
    return [FoodListSerializer.to_schema(food) for food in result]
