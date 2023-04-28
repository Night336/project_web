from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from data import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(1000))
    price = Column(Float)
    date_added = Column(DateTime, default=datetime.now)
    image = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="products")
    brand_id = Column(Integer, ForeignKey('brands.id'))
    brand = relationship("Brand", back_populates="products")

    orders = relationship("Order")
    reviews = relationship('Review', back_populates='product')

    def __init__(self, name, price, description="", img="", brand_id=None, catgory_id=None):
        self.name = name
        self.description = description
        self.price = price
        self.image = img
        if brand_id:
            self.brand_id = brand_id
        if catgory_id:
            self.category_id = catgory_id

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'date_added': self.date_added.isoformat(),
            'image': self.image,
            'category': self.category.name,
            'brand': self.brand.name
        }
