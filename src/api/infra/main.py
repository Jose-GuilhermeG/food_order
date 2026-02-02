from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.adapters.routes import category_routes, food_routes
from api.domain.exceptions import IntegrityException
from api.infra.db import create_all_tables
from api.infra.exceptions_handler import integrity_exception_handler


@asynccontextmanager
async def lifespan(app : FastAPI):
    create_all_tables()

    yield

app = FastAPI(
    lifespan=lifespan
)

#routes
app.include_router(food_routes.router)
app.include_router(category_routes.router)

#exceptions
app.add_exception_handler(IntegrityException , integrity_exception_handler)
