from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from http import HTTPStatus

from backlog_tracker.db.session import get_db
from backlog_tracker.schemas.users import UserOut, UserIn
from backlog_tracker.controllers.user_controller import UserController

router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.get(
    '/',
    response_model=List[UserOut],
    status_code=HTTPStatus.OK
)
async def get_all_users(
    db: Session = Depends(get_db),
    page: int = 1,
    limit: int | None = None,
    offset: int = 0,
):
    user_controller = UserController(db)
    all_users = user_controller.get_all_users(page, limit, offset)
    return all_users


@router.post(
    '/',
    response_model=UserOut,
    status_code=HTTPStatus.CREATED
)
async def create_user(
    user: UserIn,
    db: Session = Depends(get_db)
):
    user_controller = UserController(db)
    db_user = user_controller.get_user_by_name(user.name)
    if db_user:
        raise HTTPException(
            status_code=400, detail="User with this name already registered"
        )
    return user_controller.create_user(user)


@router.get(
    '/{user_id}',
    response_model=UserOut,
    status_code=HTTPStatus.OK
)
async def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user_controller = UserController(db)
    db_user = user_controller.get_user(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put(
    '/{user_id}',
    response_model=UserOut,
    status_code=HTTPStatus.OK
)
async def update_user(
    user_id: int,
    user: UserIn,
    db: Session = Depends(get_db)
):
    user_controller = UserController(db)
    db_user = user_controller.get_user(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_controller.update_user(user_id, user)


@router.delete(
    '/{user_id}',
    response_model=UserOut,
    status_code=HTTPStatus.OK,
    response_description='Successfully deleted user'
)
async def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user_controller = UserController(db)
    db_user = user_controller.get_user(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_controller.delete_user(user_id)
