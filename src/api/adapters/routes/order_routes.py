from asyncio import sleep
from json import loads

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, status

from api.adapters.dependencies.adpters import (
    FoodRepositoryDep,
    OrderIdentifyFactoryDep,
    OrderIdentifyRepositoryDep,
    OrderQueueDep,
)
from api.adapters.factories import OrderFactory
from api.adapters.schemas.schemas import (
    OrderIdentifyCodeSerializer,
    OrderIdentifyDetailSerializer,
    OrderIdentifyFoodSerializer,
    RegisterOrderIdentifySerializer,
)
from api.application.use_cases.order_use_case import (
    RegisterOrdersUseCase,
    SetCurrentOrderAsReady,
    ShowAllOrdersUseCase,
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
    orderfactory = OrderFactory(['order_identify' , "food"])
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

    async def get_last_ready_order(queue):
        try:
            result = ShowLastReadyOrder(repository).execute()
            await ws.send_json({"client_name" : str(result.client_name) , "code" : str(result.code) })
        except WebSocketDisconnect:
            if get_last_ready_order in orderQueue._listeners:
                orderQueue.remove_listener(get_last_ready_order)

    orderQueue.add_listener(get_last_ready_order)

    try:
        await get_last_ready_order(orderQueue)
        while True:
            await sleep(1)
    except WebSocketDisconnect:
        if get_last_ready_order in orderQueue._listeners:
            orderQueue.remove_listener(get_last_ready_order)
    finally:
        await ws.close()

@router.websocket("/")
async def list_orders_view(ws: WebSocket, repository: OrderIdentifyRepositoryDep,food_repository: FoodRepositoryDep, queue: OrderQueueDep):
    await ws.accept()

    async def show_orders(order_queue):
        try:
            result = ShowAllOrdersUseCase(repository, food_repository).execute()
            await ws.send_json([
                loads(OrderIdentifyFoodSerializer.to_schema(order).model_dump_json())
                for order in result
            ])
        except WebSocketDisconnect:
            if show_orders in queue._listeners:
                queue.remove_listener(show_orders)

    queue.add_listener(show_orders)

    try:
        await show_orders(queue)
        while True:
            await sleep(1)
    except WebSocketDisconnect:
        if show_orders in queue._listeners:
            queue.remove_listener(show_orders)
    finally:
        await ws.close()
