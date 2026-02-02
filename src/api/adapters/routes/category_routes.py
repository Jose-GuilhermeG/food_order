from fastapi import APIRouter

from api.adapters.dependencies.adpters import CategoryRepositoryDep
from api.adapters.schemas.schemas import CategoryListSerializer
from api.application.use_cases.categories_use_case import ListCategoryUseCase

router = APIRouter(
    prefix='/category',
    tags=['category']
)

@router.get(
    '/',
    response_model=list[CategoryListSerializer]
)
def list_categories_view(repository : CategoryRepositoryDep):
    result = ListCategoryUseCase(repository).execute()
    return [CategoryListSerializer.to_schema(category) for category in result]
