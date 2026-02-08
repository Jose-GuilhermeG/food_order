from typing import Generic, TypeVar

from api.domain.entities import OrderIdentify
from api.domain.exceptions import IntegrityException

T = TypeVar("T")

class Queue(
    Generic[T]
):
    def __init__(self , *items : list[T]) -> None:
        self._queue : list[T] = [*items] #type: ignore

    def enqueue(self , value : T)->None:
        self._queue.append(value)

    def dequeue(self)->T:
        if self.is_empty():
            raise IntegrityException("Queue is empty")

        return self._queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise IntegrityException("Queue is empty")
        return self._queue[0]

    def is_empty(self)->bool:
        return self.lenght == 0

    @property
    def lenght(self)->int:
        return len(self._queue)

class OrderQueue:
    _queue : Queue[OrderIdentify]
    _order_identify : int

    def __init__(self , *args):
        self._queue = Queue(*args)
        self._order_identify = 1

    def add(self , value : OrderIdentify)->OrderIdentify:
        value.code = self.get_order_identify()
        self._queue.enqueue(value)
        return value

    def get_last(self)->OrderIdentify:
        return self._queue.peek()

    def get_order_identify(self)->int:
        order_identify = self._order_identify
        self._order_identify += 1
        return order_identify

    def all(self)->list[OrderIdentify]:
        return self._queue._queue
