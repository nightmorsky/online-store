from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import all models here so that Alembic can detect them
from app.models.user import User
from app.models.category import Category
from app.models.product import Product
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.cart_item import CartItem
