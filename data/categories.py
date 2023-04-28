from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from data import Base, Product


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    products = relationship("Product")

    def __init__(self, name, description=""):
        self.name = name
        self.description = description
