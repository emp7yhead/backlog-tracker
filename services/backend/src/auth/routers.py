from datetime import timedelta
from sqlalchemy.orm import Session
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from src.auth.service import AuthUserController
from src.auth.utils import create_access_token
from src.database import get_db
from src.settings import settings


router = APIRouter(
    prefix='/login',
    tags=['login'],
)


@router.post(
    '/',
)
async def login(
    db: Session = Depends(get_db),
    user: OAuth2PasswordRequestForm = Depends()
):
    auth_user = AuthUserController(db)
    user = auth_user.validate_user(user)

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    token = jsonable_encoder(access_token)
    content = {"message": "You've successfully logged in. Welcome back!"}
    response = JSONResponse(content=content)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="Lax",
        secure=False,
    )

    return response
