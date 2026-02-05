from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.adapters.admin.routes import register_admin
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

origins = [
    "http://127.0.0.1/",
    "http://localhost:5000/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_admin(app)
