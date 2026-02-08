from sqlmodel import Session, SQLModel, create_engine

from api.adapters.queue import OrderQueue
from api.adapters.schemas import models  # noqa: F401
from api.infra.settings import DATABASE_URI

engine = create_engine(DATABASE_URI)
orderQueue = OrderQueue()

def get_session():
    with Session(engine) as session:
        yield session

def create_all_tables():
    SQLModel.metadata.create_all(engine)

def get_order_queue()->OrderQueue:
    return orderQueue
