from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from http import HTTPStatus
from sqlalchemy.exc import DatabaseError

from backlog_tracker.auth.jwthandler import OAuth2PasswordBearerCookie
from backlog_tracker.auth.controllers.password import PasswordController
from backlog_tracker.auth.schemas.jwt import TokenData
from backlog_tracker.controllers.user import UserController
from backlog_tracker.settings import Settings

security = OAuth2PasswordBearerCookie(token_url="/login")


class AuthUserController(UserController, PasswordController):

    def get_current_user(self, token: str = Depends(security)):
        credentials_exception = HTTPException(
            status_code=401,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )

        try:
            payload = jwt.decode(
                token, Settings.SECRET_KEY, algorithms=[Settings.ALGORITHM])
            username: str | None = payload.get('sub')
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except JWTError:
            raise credentials_exception

        try:
            user = self.get_user_by_username(username=token_data.username)
        except DatabaseError:
            raise credentials_exception

        return user

    def validate_user(self, user: OAuth2PasswordRequestForm = Depends()):
        try:
            db_user = self.get_user_by_username(user.username)
        except DatabaseError:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail="Incorrect username or password",
            )

        if not self.verify_password(user.password, db_user.password):
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail="Incorrect username or password",
            )

        return db_user
