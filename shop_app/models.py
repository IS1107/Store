from sqlalchemy import Boolean, Column, Integer, ForeignKey, String, Text, Float
from sqlalchemy.orm import relationship

from .db import Base


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    products = relationship("Product", back_populates="store")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    items = relationship("Item", back_populates="category")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    category_id = Column(Integer, ForeignKey("categories.id"))
    description = Column(Text)
    image_url = Column(String(255))

    category = relationship("Category", back_populates="items")
    products = relationship("Product", back_populates="item")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    store_id = Column(Integer, ForeignKey("stores.id"))
    price = Column(Float, default=0)
    active = Column(Boolean, default=False)

    item = relationship("Item", back_populates="products")
    store = relationship("Store", back_populates="products")
