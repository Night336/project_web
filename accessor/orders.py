from typing import List
import os
import sys

from accessor.base_accessor import BaseAccessor
from data import Order

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))


class OrdersAccessor(BaseAccessor):
    def get_all_orders(self) -> List[Order]:
        return self.session.query(Order).all()

    def get_all_orders_by_user_id(self, user_id: int) -> List[Order]:
        return self.session.query(Order).filter(Order.user_id == user_id).all()

    def get_orders_by_id(self, orders_id: int) -> Order:
        return self.session.query(Order).get(orders_id)

    def create_orders(self, quantity: int, user_id: int, product_id: int) -> Order:
        orders = Order(quantity=quantity, user_id=user_id, product_id=product_id)
        self.session.add(orders)
        self.session.commit()
        self.session.refresh(orders)
        return orders

    def update_orders(self, orders_id: int, quantity: int) -> Order:
        orders = self.session.query(Order).get(orders_id)
        orders.quantity = quantity
        self.session.commit()
        self.session.refresh(orders)
        return orders

    def delete_orders(self, orders_id: int) -> None:
        self.session.query(Order).filter(Order.id == orders_id).delete()
        self.session.commit()
