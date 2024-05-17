# sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, DateTime, Table, String, Boolean, Text, Float
from datetime import datetime

# base
from app.core.db.base import Base


class Product(Base):
    title = Column(String, nullable = False)
    supplier = Column(String, nullable = False)
    price = Column(Float, nullable = False)
    image_url = Column(String, nullable = False)
    description = Column(String, nullable = False)
    quantity = Column(Integer, nullable = False)
    