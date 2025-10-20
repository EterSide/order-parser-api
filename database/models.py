"""
데이터베이스 모델 정의
"""
from sqlalchemy import (
    Column, BigInteger, String, Text, Integer, 
    Numeric, DateTime, Boolean, Enum, ForeignKey
)
from sqlalchemy.orm import relationship
from datetime import datetime
from database.connection import Base
import enum


class OrderStatus(enum.Enum):
    """주문 상태"""
    PENDING = "PENDING"
    PREPARING = "PREPARING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class PaymentMethod(enum.Enum):
    """결제 방법"""
    CASH = "CASH"
    CARD = "CARD"
    MOBILE = "MOBILE"


class Category(Base):
    """카테고리 테이블"""
    __tablename__ = "categories"
    
    category_id = Column(BigInteger, primary_key=True, autoincrement=True)
    category_name = Column(String(50), nullable=False, unique=True)
    category_eng_name = Column(String(50), unique=True)
    display_order = Column(Integer, nullable=False)
    created_at = Column(DateTime(6), default=datetime.utcnow)
    
    # 관계
    product_categories = relationship("ProductCategory", back_populates="category")


class Product(Base):
    """제품 테이블"""
    __tablename__ = "products"
    
    product_id = Column(BigInteger, primary_key=True, autoincrement=True)
    product_name = Column(String(100), nullable=False)
    product_eng_name = Column(String(100))
    description = Column(Text)
    eng_description = Column(String(255))
    price = Column(Numeric(10, 2), nullable=False)
    image_url = Column(String(255))
    is_available = Column(Boolean, default=True)
    created_at = Column(DateTime(6), default=datetime.utcnow)
    updated_at = Column(DateTime(6), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 관계
    product_categories = relationship("ProductCategory", back_populates="product")
    product_option_groups = relationship("ProductOptionGroup", back_populates="product")
    order_items = relationship("OrderItem", back_populates="product")


class ProductCategory(Base):
    """제품-카테고리 연결 테이블"""
    __tablename__ = "product_categories"
    
    product_category_id = Column(BigInteger, primary_key=True, autoincrement=True)
    product_id = Column(BigInteger, ForeignKey("products.product_id"), nullable=False)
    category_id = Column(BigInteger, ForeignKey("categories.category_id"), nullable=False)
    display_order = Column(Integer)
    created_at = Column(DateTime(6), default=datetime.utcnow)
    
    # 관계
    product = relationship("Product", back_populates="product_categories")
    category = relationship("Category", back_populates="product_categories")


class OptionGroup(Base):
    """옵션 그룹 테이블"""
    __tablename__ = "option_groups"
    
    option_group_id = Column(BigInteger, primary_key=True, autoincrement=True)
    group_name = Column(String(50), nullable=False)
    is_required = Column(Boolean, default=False)
    max_selection = Column(Integer)
    created_at = Column(DateTime(6), default=datetime.utcnow)
    
    # 관계
    options = relationship("Option", back_populates="option_group")
    product_option_groups = relationship("ProductOptionGroup", back_populates="option_group")


class Option(Base):
    """옵션 테이블"""
    __tablename__ = "options"
    
    option_id = Column(BigInteger, primary_key=True, autoincrement=True)
    option_group_id = Column(BigInteger, ForeignKey("option_groups.option_group_id"), nullable=False)
    option_name = Column(String(50), nullable=False)
    additional_price = Column(Numeric(10, 2), default=0)
    created_at = Column(DateTime(6), default=datetime.utcnow)
    
    # 관계
    option_group = relationship("OptionGroup", back_populates="options")
    order_item_options = relationship("OrderItemOption", back_populates="option")


class ProductOptionGroup(Base):
    """제품-옵션그룹 연결 테이블"""
    __tablename__ = "product_option_groups"
    
    product_option_group_id = Column(BigInteger, primary_key=True, autoincrement=True)
    product_id = Column(BigInteger, ForeignKey("products.product_id"), nullable=False)
    option_group_id = Column(BigInteger, ForeignKey("option_groups.option_group_id"), nullable=False)
    created_at = Column(DateTime(6), default=datetime.utcnow)
    
    # 관계
    product = relationship("Product", back_populates="product_option_groups")
    option_group = relationship("OptionGroup", back_populates="product_option_groups")


class Order(Base):
    """주문 테이블"""
    __tablename__ = "orders"
    
    order_id = Column(BigInteger, primary_key=True, autoincrement=True)
    order_number = Column(String(20), nullable=False, unique=True)
    order_status = Column(Enum(OrderStatus), nullable=False)
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    total_amount = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime(6), default=datetime.utcnow)
    updated_at = Column(DateTime(6), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 관계
    order_items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    """주문 항목 테이블"""
    __tablename__ = "order_items"
    
    order_item_id = Column(BigInteger, primary_key=True, autoincrement=True)
    order_id = Column(BigInteger, ForeignKey("orders.order_id"), nullable=False)
    product_id = Column(BigInteger, ForeignKey("products.product_id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=False)
    subtotal = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime(6), default=datetime.utcnow)
    
    # 관계
    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")
    order_item_options = relationship("OrderItemOption", back_populates="order_item")


class OrderItemOption(Base):
    """주문 항목 옵션 테이블"""
    __tablename__ = "order_item_options"
    
    order_item_option_id = Column(BigInteger, primary_key=True, autoincrement=True)
    order_item_id = Column(BigInteger, ForeignKey("order_items.order_item_id"), nullable=False)
    option_id = Column(BigInteger, ForeignKey("options.option_id"), nullable=False)
    additional_price = Column(Numeric(10, 2), default=0)
    created_at = Column(DateTime(6), default=datetime.utcnow)
    
    # 관계
    order_item = relationship("OrderItem", back_populates="order_item_options")
    option = relationship("Option", back_populates="order_item_options")

