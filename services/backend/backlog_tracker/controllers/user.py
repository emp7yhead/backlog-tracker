from typing import List
from sqlalchemy import delete, select, update
from passlib.context import CryptContext

from backlog_tracker.models.user import User
from backlog_tracker.schemas.users import UserIn, UserOut

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserController:
    def __init__(self, session):
        self.session = session

    def get_user(self, user_id: int) -> UserOut:
        user = self.session.get(User, user_id)
        return user

    def get_user_by_username(self, username: str) -> UserOut:
        user = self.session.execute(
            select(User).
            where(User.username == username)
        ).all()
        return user

    def get_all_users(self, page, limit, offset) -> List[UserOut]:
        all_users = self.session.scalars(
            select(User).
            limit(limit).
            offset(offset * (page - 1))
        ).all()
        return all_users

    def create_user(self, user: UserIn) -> UserOut:
        user.password = password_context.hash(user.password)
        new_user = User(**user.dict())
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def update_user(self, user_id: int, user: UserIn) -> UserOut:
        user_to_update = self.session.get(User, user_id)
        self.session.execute(
            update(User).
            where(User.id == user_id).
            values(
                User.username == user.username,
                User.password == password_context.hash(user.password),
            ).
            execution_options(
                synchronize_session="evaluate"
            )
        )
        # user_to_update.username = user.username
        # user_to_update.password = password_context.encrypt(user.password)
        # self.session.add(user_to_update)
        # self.session.commit()
        return user_to_update

    def delete_user(self, user_id: int) -> UserOut:
        user = self.session.get(User, user_id)
        self.session.execute(
            delete(User)
            .where(User.id == user_id)
            .execution_options(synchronize_session="fetch")
        )
        self.session.commit()
        return user
