from fastapi import APIRouter, Request

router = APIRouter(
    tags=['index'],
)


@router.get('/')
async def index(request: Request):
    return "Hello, Backlog Tracker!"
