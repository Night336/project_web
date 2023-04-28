from typing import List
import os
import sys

from accessor.base_accessor import BaseAccessor
from data import Product

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))


class ProductAccessor(BaseAccessor):
    def get_all_product(self) -> List[Product]:
        return self.session.query(Product).all()

    def get_product_by_id(self, product_id: int) -> Product:
        return self.session.query(Product).get(product_id)

    def get_all_product_by_category(self, category_id: int):
        return self.session.query(Product).filter(Product.category_id == category_id).all()

    def get_name_by_id(self, name: str):
        return self.session.query(Product).get(name)

    def get_price_by_id(self, price: int):
        return self.session.query(Product).get(price)

    def create_product(self, name: str, price: int) -> Product:
        product = Product(name=name, price=price)
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product

    def create_product_from_form(self, form):
        name = form.get("name")
        description = form.get("description")
        price = form.get("price")
        img = ""
        category = form.get("category")
        brand = form.get("brand")
        product = Product(name=name, price=price, description=description, img=img, brand_id=brand, catgory_id=category)
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product

    def update_product(self, product_id: int, name: str, price: int) -> Product:
        product = self.session.query(Product).get(product_id)
        product.name = name
        product.price = price
        self.session.commit()
        self.session.refresh(product)
        return product

    def delete_product(self, product_id: int) -> None:
        self.session.query(Product).filter(Product.id == product_id).delete()
        self.session.commit()
