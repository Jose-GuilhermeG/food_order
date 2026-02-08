from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from api.adapters.queue import OrderQueue
from api.infra.db import get_order_queue, get_session

SessionDep = Annotated[Session , Depends(get_session)]
OrderQueueDep = Annotated[OrderQueue , Depends(get_order_queue)]
