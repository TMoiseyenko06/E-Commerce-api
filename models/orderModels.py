from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from typing import List
from .productModels import Product

order_products = Table(
    'order_products',
    Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.id'),primary_key=True),
    Column('product_id', Integer, ForeignKey('products.id'),primary_key=True)
)

class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'))
    products: Mapped[List[Product]] = relationship(Product,secondary=order_products)

