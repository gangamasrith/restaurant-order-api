from sqlalchemy import Column, Integer, String, Float
from database import Base


class Menu(Base):
    __tablename__ = "menu"

    item_id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String)
    cat_id = Column(Integer)
    menu_id = Column(Integer)
    size = Column(String)
    price = Column(String)


class OrderHistory(Base):
    __tablename__ = "order_history"

    id = Column(Integer, primary_key=True, index=True)
    order_date = Column(String)
    order_id = Column(Integer)
    item_id = Column(Integer)
    size = Column(String)
    price = Column(Float)
    qty = Column(Integer)
    order_status = Column(String)
    total = Column(Float)


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    payment_date = Column(String)
    payment_id = Column(Integer)
    order_id = Column(Integer)
    amount_due = Column(Float)
    tips = Column(Float)
    discount = Column(Float)
    total_paid = Column(Float)
    payment_type = Column(String)
    payment_status = Column(String)