from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from ..db import Base
from datetime import datetime



class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, nullable=True)
    cpf = Column(String, unique=True, nullable=True)

    hashed_password = Column(String, nullable=False)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)

    two_fa_secret = Column(String, nullable=True)  # 2FA
    reset_code = Column(String, nullable=True)     # Código de reset de senha

    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    accounts = relationship("Accounts", back_populates="user", cascade="all, delete")

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"