import pytest

from api.adapters.factories import FoodFactory
from api.adapters.mapping import FoodMapping
from api.domain.enums import OrderStatus


@pytest.fixture
def simple_category_data():
    return {
        "id": 1,
        "name": "Bebidas",
        "slug": "Bebidas",
    }

@pytest.fixture
def simple_food_data():
    return {
        "id": 10,
        "name": "Suco de Laranja",
        "slug": "Suco Natural",
        "description": "Suco fresco e natural",
        "price": 5.50,
        "photos" : []
    }

@pytest.fixture
def simple_order_data():
    return {
        "order_identify": 100,
        "food_id": 10,
        "quantity": 2,
        "status": OrderStatus.PENDING.value,
    }

@pytest.fixture
def simple_order_identify_data():
    return {
        "code": 999,
        "client_name": "Maria",
    }

@pytest.fixture
def food_factory():
    return FoodFactory()

@pytest.fixture
def food_mapping(food_factory):
    return FoodMapping(food_factory)
