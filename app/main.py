from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config.database import init_db
from app.middleware.app_middleware import add_middlewares
from app.routers import auth_routes, project_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)

add_middlewares(app)

app.include_router(auth_routes.router)
app.include_router(project_routes.router)


@app.get("/")
async def root() -> dict:
    return {
        "message": "Coding Sphere Assignment -- FastAPI app with RBAC",
        "description": "Submitted by George Louis"
    }