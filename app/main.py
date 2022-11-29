from fastapi import FastAPI

from app.routers import index

app = FastAPI()

app.include_router(index.router)
