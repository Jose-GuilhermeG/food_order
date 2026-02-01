from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.infra.db import create_all_tables


@asynccontextmanager
async def lifespan(app : FastAPI):
    create_all_tables()

    yield

app = FastAPI(
    lifespan=lifespan
)
