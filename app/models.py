from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.database import Base


class Product(Base):
    """
    Universal Product Table

    Works for:
    - Grocery
    - Electronics
    - Furniture
    - Books
    - Pharmacy
    - Fashion
    - Warehouse Inventory
    - Automobile Parts
    - etc.
    """

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    product_name = Column(String, nullable=False, index=True)

    brand = Column(String, nullable=True)

    category = Column(String, nullable=True)

    supplier = Column(String, nullable=True)

    description = Column(String, nullable=True)

    price = Column(Float, nullable=False)

    stock = Column(Integer, nullable=True)

    rating = Column(Float, nullable=True)

    uploaded_at = Column(DateTime, default=datetime.utcnow)