from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(index=True)
    description: Mapped[str]
    price: Mapped[float]
    image_url: Mapped[str]
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    quantity: Mapped[int] = mapped_column(default=0)