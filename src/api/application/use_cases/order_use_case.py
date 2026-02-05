from api.application.interfaces.factories import IOrderIdentifyFactory
from api.application.interfaces.repositories import (
    IOrderIdentifyRepository,
    IOrderRepository,
)
from api.domain.entities import Order, OrderIdentify


class RegisterOrdersUseCase:
    def __init__(self , order_identify_repository : IOrderIdentifyRepository , factory :IOrderIdentifyFactory , order_repository : IOrderRepository ):
        self.order_identify_repository = order_identify_repository
        self.factory = factory
        self.order_repository = order_repository

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
