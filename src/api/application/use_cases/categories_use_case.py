from api.application.interfaces.repositories import ICategoryRepository
from api.domain.entities import Category


class ListCategoryUseCase:
    def __init__(self , repository : ICategoryRepository):
        self.repository = repository

    def execute(self) -> list[Category]:
        return self.repository.all()

class CategoryDetailUseCase:
    def __init__(self , repository : ICategoryRepository):
        self.repository = repository

    def execute(self , slug : str)->Category:
        return self.repository.get_by_slug(slug)
