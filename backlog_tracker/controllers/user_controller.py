from backlog_tracker.models.user import User
from backlog_tracker.schemas.users import UserBase


class UserController:
    def __init__(self, session):
        self.session = session

    def get_user(self, user_id: int):
        user = self.session.query(User).get(user_id)
        return user

    def get_user_by_name(self, name: str):
        user = self.session.query(User).filter(User.name == name).first()
        return user

    def create_user(self, user: UserBase):
        self.session.add(user)
        self.session.commit()
        return user

    def update_user(self, user_id: int, user: UserBase):
        user_to_update = self.session.query(User).get(user_id)
        user_to_update.name = user.name
        self.session.add(user)
        self.session.commit()
        return user_to_update

    def delete_user(self, user_id: int):
        user = self.session.query(User).get(user_id)
        self.session.delete(user)
        self.session.commit()
        return {"status": "ok"}
