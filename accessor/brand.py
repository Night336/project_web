from typing import List
import os
import sys

from accessor.base_accessor import BaseAccessor

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))
from data import Brand


class BrandAccessor(BaseAccessor):
    def get_all_brands(self) -> List[Brand]:
        return self.session.query(Brand).all()

    def get_brand_by_id(self, brand_id: int) -> Brand:
        return self.session.query(Brand).get(brand_id)

    def create_brand(self, name: str) -> Brand:
        brand = Brand(name=name)
        self.session.add(brand)
        self.session.commit()
        self.session.refresh(brand)
        return brand

    def update_brand(self, brand_id: int, name: str) -> Brand:
        brand = self.session.query(Brand).get(brand_id)
        brand.name = name
        self.session.commit()
        self.session.refresh(brand)
        return brand

    def delete_brand(self, brand_id: int) -> None:
        self.session.query(Brand).filter(Brand.id == brand_id).delete()
        self.session.commit()
