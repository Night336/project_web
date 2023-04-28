import os
import sys

from .base_accessor import BaseAccessor
from data import Category

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))


class CategoryAccessor(BaseAccessor):
    def get_category_by_id(self, category_id: int):
        return self.session.query(Category).filter(Category.id == category_id).first()

    def get_all_categories(self):
        return self.session.query(Category).all()

    def get_category_by_name(self, category_name: str):
        return self.session.query(Category).filter(Category.name == category_name).first()

    def create_category(self, name: str, description: str):
        categories = self.get_category_by_name(name)
        if not categories:
            categories = Category(name=name, description=description)
            self.session.add(categories)
            self.session.commit()
        return categories
