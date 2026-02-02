import pytest

from api.domain.entities import Category, Food, Order, OrderIdentify
from api.domain.enums import OrderStatus
from api.domain.exceptions import (
    EmptyValidationException,
    IdValidationException,
    ValidationException,
)

#this tests are made with AI , it will be refactore later

class TestCategory:
    def test_id_validation(self):
        c = Category()
        c.id = 1
        assert c.id == 1

        with pytest.raises(IdValidationException):
            c.id = -1

    def test_name_validation(self):
        c = Category()
        c.name = "Bebidas"
        assert c.name == "Bebidas"

        with pytest.raises(EmptyValidationException):
            c.name = ""

    def test_slug_validation_and_transformation(self):
        c = Category()
        c.slug = "Bebidas"
        assert c.slug == "bebidas"

        c.slug = "Água Mineral"
        assert c.slug == "água-mineral"

        with pytest.raises(EmptyValidationException):
            c.slug = ""

    def test_image_validation(self):
        c = Category()
        c.image = "https://exemple_photo"

        with pytest.raises(ValidationException):
            c.image = 5

    def test_str_representation(self, simple_category):
        assert str(simple_category) == "Bebidas"


class TestFood:
    def test_id_validation(self):
        f = Food()
        f.id = 1
        assert f.id == 1

        with pytest.raises(IdValidationException):
            f.id = -10

    def test_name_validation(self):
        f = Food()
        f.name = "Pizza"
        assert f.name == "Pizza"

        with pytest.raises(EmptyValidationException):
            f.name = ""

    def test_slug_validation_and_transformation(self):
        f = Food()
        f.slug = "Pizza"
        assert f.slug == "pizza"

        f.slug = "Pizza Calabresa"
        assert f.slug == "pizza-calabresa"

        with pytest.raises(EmptyValidationException):
            f.slug = ""

    def test_description_validation(self):
        f = Food()
        f.description = "Pizza com queijo e calabresa"
        assert f.description == "Pizza com queijo e calabresa"

        with pytest.raises(ValidationException):
            f.description = 12345

    def test_price_validation(self):
        f = Food()
        f.price = 29.90
        assert f.price == 29.90

        with pytest.raises(ValidationException):
            f.price = -5.0

    def test_str_representation(self):
        f = Food()
        f.name = "Pizza"
        f.price = 29.90
        assert str(f) == "Pizza - R$29.90"


class TestOrder:
    def test_order_identify_validation(self):
        o = Order()
        o.order_identify = 10
        assert o.order_identify == 10

        with pytest.raises(IdValidationException):
            o.order_identify = "abc"

        with pytest.raises(IdValidationException):
            o.order_identify = -1

    def test_food_id_validation(self):
        o = Order()
        o.food_id = 5
        assert o.food_id == 5

        with pytest.raises(IdValidationException):
            o.food_id = 3.5

        with pytest.raises(IdValidationException):
            o.food_id = -2

    def test_quantity_validation(self):
        o = Order()
        o.quantity = 3
        assert o.quantity == 3

        with pytest.raises(ValidationException):
            o.quantity = 0

        with pytest.raises(ValidationException):
            o.quantity = -5

    def test_status_validation(self):
        o = Order()
        o.status = OrderStatus.PENDING.value
        assert o.status == OrderStatus.PENDING.value

        o.status = "Confirmado"
        assert o.status == "Confirmado"

        with pytest.raises(ValidationException):
            o.status = "invalid_status"

    def test_str_representation(self):
        o = Order()
        o.order_identify = 1
        o.food_id = 10
        o.quantity = 2
        o.status = OrderStatus.PENDING.value
        assert str(o) == f"Order 1 - Food 10 x 2 [{OrderStatus.PENDING.value}]"

class TestOrderIdentify:
    def test_code_validation(self):
        o = OrderIdentify()
        o.code = 100
        assert o.code == 100

        with pytest.raises(IdValidationException):
            o.code = "abc"

        with pytest.raises(IdValidationException):
            o.code = -5

    def test_client_name_validation(self):
        o = OrderIdentify()
        o.client_name = "João"
        assert o.client_name == "João"

        with pytest.raises(ValidationException):
            o.client_name = None

        with pytest.raises(EmptyValidationException):
            o.client_name = ""

    def test_str_representation(self):
        o = OrderIdentify()
        o.code = 123
        o.client_name = "Maria"
        assert str(o) == f"Order Code: 123 - Client: Maria"
