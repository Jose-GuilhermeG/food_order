from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.adapters.routes import food_routes
from api.infra.db import create_all_tables


@asynccontextmanager
async def lifespan(app : FastAPI):
    create_all_tables()

    yield

app = FastAPI(
    lifespan=lifespan
)

#routes
app.include_router(food_routes.router)
