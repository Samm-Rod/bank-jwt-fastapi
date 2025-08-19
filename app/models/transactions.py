from datetime import datetime
from sqlalchemy import Boolean, ForeignKey, Integer, String, Float, DateTime, Column, Enum
from sqlalchemy.orm import relationship
from ..db import Base
from ..enuns import TransactionType

class Transactions(Base):
    __tablename__="transactons"
    
    id = Column(Integer, primary_key=True, index=True)
    accouunt_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    amount = Column(Float, nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    date = Column(DateTime, default=datetime.now)
    descricao = Column(String)

    account = relationship("Account", back_populates="transactions")