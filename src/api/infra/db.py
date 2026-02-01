from sqlmodel import Session, SQLModel, create_engine

from api.adapters.schemas import models  # noqa: F401
from api.infra.settings import DATABASE_URI

engine = create_engine(DATABASE_URI)

def get_session():
    with Session(engine) as session:
        yield session

def create_all_tables():
    SQLModel.metadata.create_all(engine)
