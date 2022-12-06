from fastapi import Depends, APIRouter, HTTPException
from pytest import Session

from backlog_tracker.db.session import get_db
from backlog_tracker.schemas.users import User, UserBase
from backlog_tracker.controllers.user_controller import UserController

router = APIRouter()


@router.get('/users/{user_id}', response_model=User)
async def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user_controller = UserController(db)
    db_user = user_controller.get_user(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post('/users', response_model=User)
async def create_user(
    user: UserBase,
    db: Session = Depends(get_db)
):
    user_controller = UserController(db)
    db_user = user_controller.get_user_by_name(user.name)
    if db_user:
        raise HTTPException(
            status_code=400, detail="User with this name already registered"
        )
    return user_controller.create_user(user)


@router.put('/users/{user_id}', response_model=User)
async def update_user(
    user_id: int,
    user: UserBase,
    db: Session = Depends(get_db)
):
    user_controller = UserController(db)
    db_user = user_controller.get_user(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_controller.update_user(user_id, user)


@router.delete('/users/{user_id}', response_model=User)
async def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user_controller = UserController(db)
    db_user = user_controller.get_user(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_controller.delete_user(user_id)
