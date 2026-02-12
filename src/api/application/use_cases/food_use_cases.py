from api.application.interfaces.repositories import ICategoryRepository, IFoodRepository
from api.domain.entities import Food
from api.domain.exceptions import IntegrityException


class ListFoodUseCase:
    def __init__(self , repository : IFoodRepository ):
        self.repository = repository

    def execute(self)->list[Food]:
        result = self.repository.all()
        return result

class FoodDetailUseCase:
    def __init__(self , repository : IFoodRepository ):
       self.repository = repository

    def execute(self , slug : str)->Food:
        return self.repository.get_by_slug(slug)

class SearchFoodUseCase:
    def __init__(self , repository : IFoodRepository , category_repository : ICategoryRepository):
        self.repository = repository
        self.category_repository = category_repository

    def execute(self , query : str , category_slug : str )->list[Food]:
        if not self.category_repository.exist_by_slug(category_slug):
            raise IntegrityException("that category does not exist")

        return self.repository.search(query , category_slug)
