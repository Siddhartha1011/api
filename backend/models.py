from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, ForeignKey, CheckConstraint
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(100), unique=True, nullable=False)

    total_amount = Column(Numeric(15, 2), default=0)
    transaction_count = Column(Integer, default=0)
    score = Column(Numeric(10, 2), default=0)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)

    transaction_id = Column(String(120), unique=True, nullable=False)

    user_pk = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    amount = Column(Numeric(15, 2), nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())