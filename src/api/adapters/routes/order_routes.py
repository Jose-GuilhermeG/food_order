from asyncio import sleep

from fastapi import APIRouter, WebSocket, status

from api.adapters.dependencies.adpters import (
    OrderIdentifyFactoryDep,
    OrderIdentifyRepositoryDep,
    OrderQueueDep,
)
from api.adapters.factories import OrderFactory
from api.adapters.schemas.schemas import (
    OrderIdentifyCodeSerializer,
    OrderIdentifyDetailSerializer,
    RegisterOrderIdentifySerializer,
)
from api.application.use_cases.order_use_case import (
    RegisterOrdersUseCase,
    SetCurrentOrderAsReady,
    ShowCurrentOrderUseCase,
    ShowLastReadyOrder,
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
    repository._queue.commit() #type: ignore
    return OrderIdentifyCodeSerializer.to_schema(result)

@router.post(
    '/ready/',
    tags=["ready"],
    status_code=status.HTTP_204_NO_CONTENT
)
def set_current_order_as_ready(repository : OrderIdentifyRepositoryDep ):
    SetCurrentOrderAsReady(repository).execute()
    return

@router.websocket(
    "/ready/",
)
async def show_last_ready_order(repository : OrderIdentifyRepositoryDep , ws : WebSocket , orderQueue : OrderQueueDep):
    await ws.accept()

    async def get_response(queue):
        try:
            result = ShowLastReadyOrder(repository).execute()
            await ws.send_json({"client_name" : str(result.client_name) , "code" : str(result.code) })
        except Exception :
            await sleep(0.1)

    orderQueue.add_listener(get_response)

    try:
        while True:
            await sleep(0.1)
    except Exception:
        await ws.close()
    finally:
        if get_response in orderQueue._listeners:
            orderQueue.remove_listener(get_response)

        await ws.close()
