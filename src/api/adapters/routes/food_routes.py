from fastapi import APIRouter

from api.adapters.dependencies.adpters import FoodRepositoryDep
from api.adapters.schemas.schemas import FoodListSerializer, FoodSerializer
from api.application.use_cases.food_use_cases import FoodDetailUseCase, ListFoodUseCase

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
def detail_food_view(slug : str , food_repository : FoodRepositoryDep):
    result = FoodDetailUseCase(food_repository).execute(slug)
    return FoodSerializer.to_schema(result)
