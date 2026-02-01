from api.application.interfaces.repositories import IFoodRepository
from api.domain.entities import Food


class ListFoodUseCase:
    def __init__(self , repository : IFoodRepository ):
        self.repository = repository

    def execute(self)->list[Food]:
        result = self.repository.all()
        return result
