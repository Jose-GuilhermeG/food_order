from fastapi import APIRouter

from api.adapters.dependencies.adpters import FoodRepositoryDep
from api.adapters.schemas.schemas import FoodListSerializer
from api.application.use_cases.food_use_cases import ListFoodUseCase

router = APIRouter(
    prefix='/food',
    tags=['food']
)

@router.get(
    '/',
    response_model=list[FoodListSerializer  ]
)
def list_food_view(food_repository : FoodRepositoryDep):
    result = ListFoodUseCase(food_repository).execute()
    return [ FoodListSerializer( name=food.name, description=food.description, price=food.price, slug = food.slug , ) for food in result ]
