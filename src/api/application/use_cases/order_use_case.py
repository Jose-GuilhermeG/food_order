from api.application.interfaces.factories import IOrderIdentifyFactory
from api.application.interfaces.repositories import (
    IFoodRepository,
    IOrderIdentifyRepository,
)
from api.domain.entities import Food, Order, OrderIdentify


class RegisterOrdersUseCase:
    def __init__(self , order_identify_repository : IOrderIdentifyRepository , factory :IOrderIdentifyFactory ):
        self.order_identify_repository = order_identify_repository
        self.factory = factory
        self.factory._ignore_attrs = ["code"]

    def execute(self , orders : list[Order] , client_name : str ) -> OrderIdentify:

        order_identify = self.order_identify_repository.create(self.factory.create(
            client_name=client_name,
            orders = []
        ))

        for order in orders:
            order.order_identify = order_identify.code

        order_identify.orders = orders

        self.order_identify_repository.save(order_identify)

        return order_identify

class ShowCurrentOrderUseCase:
    def __init__(self , repository : IOrderIdentifyRepository):
        self.repository = repository

    def execute(self)->OrderIdentify:
        return self.repository.get_last()

class SetCurrentOrderAsReady:
    def __init__(self , repository : IOrderIdentifyRepository):
        self.repository = repository

    def execute(self)->None:
        return self.repository.set_current_order_as_ready()

class ShowLastReadyOrder:
    def __init__(self , repository : IOrderIdentifyRepository):
        self.repository = repository

    def execute(self)->OrderIdentify:
        return self.repository.get_last_ready()

class ShowAllOrdersUseCase:
    def __init__(self , repository : IOrderIdentifyRepository , food_repository : IFoodRepository):
        self.repository = repository
        self.food_repository = food_repository

    def execute(self)->list[OrderIdentify]:
        orders = self.repository.get_all()
        food_ids = self.get_food_ids(orders)
        foods = self.food_repository.get_by_id_in_list(food_ids)
        self.set_food_in_order(foods , orders)
        return orders

    def get_food_ids(self , orders : list[OrderIdentify]):
        food_ids = set()
        for orderIdentify in orders:
            for order in orderIdentify.orders:
                food_ids.add(order.food_id)
        return food_ids

    def set_food_in_order(self , foods : list[Food] , orders : list[OrderIdentify])->None:
        for orderIdentify in orders:
            for order in orderIdentify.orders:
                order_food_id = order.food_id
                food = [food for food in foods if food.id == order_food_id][0]
                order.food = food
