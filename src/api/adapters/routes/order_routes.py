from fastapi import APIRouter

from api.adapters.dependencies.adpters import (
    OrderIdentifyFactoryDep,
    OrderIdentifyRepositoryDep,
)
from api.adapters.factories import OrderFactory
from api.adapters.schemas.schemas import (
    OrderIdentifyCodeSerializer,
    OrderIdentifyDetailSerializer,
    RegisterOrderIdentifySerializer,
)
from api.application.use_cases.order_use_case import (
    RegisterOrdersUseCase,
    ShowCurrentOrderUseCase,
)

router = APIRouter(
    prefix='/orders',
    tags=['Orders']
)

@router.get(
    '/current-order/',
    response_model=OrderIdentifyDetailSerializer
)
def show_current_order_view(repository : OrderIdentifyRepositoryDep):
    result = ShowCurrentOrderUseCase(repository).execute()
    return OrderIdentifyDetailSerializer.to_schema(result)

@router.post(
    '/',
    response_model=OrderIdentifyCodeSerializer
)
def register_order_view(data : RegisterOrderIdentifySerializer , repository : OrderIdentifyRepositoryDep , factory : OrderIdentifyFactoryDep)->dict[str , int]:
    orderfactory = OrderFactory(['order_identify'])
    orders_data = data.model_dump().get("orders" , [])
    orders = []
    for order in orders_data:
        orders.append(orderfactory.create(**order))
    result = RegisterOrdersUseCase(repository , factory).execute(orders , data.client_name) #type: ignore
    return OrderIdentifyCodeSerializer.to_schema(result)
