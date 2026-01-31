import pytest
from api.domain.entities import Category, Food, Order, OrderIdentify
from api.domain.enums import OrderStatus

@pytest.fixture
def simple_category():
    c = Category()
    c.id = 1
    c.name = "Bebidas"
    c.slug = "Bebidas"
    return c

@pytest.fixture
def simple_food():
    f = Food()
    f.id = 10
    f.name = "Suco de Laranja"
    f.slug = "Suco Natural"
    f.description = "Suco fresco e natural"
    f.price = 5.50
    return f

@pytest.fixture
def simple_order():
    o = Order()
    o.order_identify = 100
    o.food_id = 10
    o.quantity = 2
    o.status = OrderStatus.PENDING.value
    return o

@pytest.fixture
def simple_order_identify():
    oi = OrderIdentify()
    oi.code = 999
    oi.client_name = "Maria"
    return oi
