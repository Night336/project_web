import os
import sys

from .base_accessor import BaseAccessor

from data import User

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))


class UserAccessor(BaseAccessor):
    def get_user_by_id(self, category_id: int):
        return self.session.query(User).filter(User.id == category_id).first()

    def get_user_by_email(self, email: str) -> User:
        return self.session.query(User).filter(User.email == email).first()

    def get_all_users(self):
        return self.session.query(User).all()

    def create_user(self, email: str, password: str):
        user = self.get_user_by_email(email)
        if not user:
            user = User(email, password)
            self.session.add(user)
            self.session.commit()
        return user
