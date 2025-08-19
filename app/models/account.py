from datetime import datetime
from sqlalchemy import Boolean, ForeignKey, Integer, String, Float, DateTime, Column
from sqlalchemy.orm import relationship
from ..db import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    account_number = Column(Integer, nullable=False)
    account_type = Column(String, nullable=False)
    balance = Column(Float, nullable=False)
    is_activate = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)

    user = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")
