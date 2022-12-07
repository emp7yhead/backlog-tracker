from backlog_tracker.models.user import User
from backlog_tracker.schemas.users import UserIn


class UserController:
    def __init__(self, session):
        self.session = session

    def get_user(self, user_id: int):
        user = self.session.query(User).get(user_id)
        return user

    def get_user_by_name(self, name: str):
        user = self.session.query(User).filter(User.name == name).first()
        return user

    def get_all_users(self, page, limit, offset):
        all_users = self.session.query(User).limit(limit).offset(
            offset * (page - 1)
        ).all()
        return all_users

    def create_user(self, user: UserIn):
        new_user = User(**user.dict())
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def update_user(self, user_id: int, user: UserIn):
        user_to_update = self.session.query(User).get(user_id)
        user_to_update.name = user.name
        self.session.add(user_to_update)
        self.session.commit()
        return user_to_update

    def delete_user(self, user_id: int):
        user = self.session.query(User).get(user_id)
        self.session.delete(user)
        self.session.commit()
        return user
