from fastapi import FastAPI
from backlog_tracker.routers import index, users

app = FastAPI()

app.include_router(index.router)
app.include_router(users.router)
