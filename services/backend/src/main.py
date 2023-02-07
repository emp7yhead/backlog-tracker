from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.auth import routers
from src.users import routers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.router)


@app.get(
    '/',
    tags=['index'],
)
async def index(request: Request):
    return "Hello, Backlog Tracker!"
