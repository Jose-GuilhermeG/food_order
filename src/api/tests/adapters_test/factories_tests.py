import pytest

from api.application.interfaces.factories import IFoodFactory
from api.domain.entities import Food
from api.domain.exceptions import (
    EmptyValidationException,
    IdValidationException,
    ValidationException,
)


class TestFoodFactory:
    def test_if_create_instance_data_is_correct(self , simple_food_data : dict , food_factory : IFoodFactory):
        factory_instance = food_factory.create(**simple_food_data)
        assert factory_instance.id  == simple_food_data.get("id")
        assert factory_instance.name  == simple_food_data.get("name")
        assert factory_instance.description  == simple_food_data.get("description")
        assert factory_instance.photos  == simple_food_data.get("photos")
        assert factory_instance.price  == simple_food_data.get("price")
        assert factory_instance.slug  == simple_food_data.get("slug").lower().replace(" ","_")

    def test_if_create_instance_raise_validate_exception_with_icorrect_data(self , food_factory : IFoodFactory):
        incorrect_data = {'id' : -10 , "name" : None , "description" : 10 , "slug" : "" , "photos" : dict() , "price" : -50}

        with pytest.raises((IdValidationException , EmptyValidationException , ValidationException)):
            food_factory.create(**incorrect_data)
