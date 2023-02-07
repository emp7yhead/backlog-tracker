from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.auth.routers import auth_router
from src.users.routers import users_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)


@app.get(
    '/',
    tags=['index'],
)
async def index(request: Request):
    return "Hello, Backlog Tracker!"
