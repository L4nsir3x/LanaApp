from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean
from sqlalchemy.sql import func
from Lana_App.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id           = Column(Integer, primary_key=True, index=True)
    amount       = Column(Float,   nullable=False)
    description  = Column(String(256), nullable=True)
    timestamp    = Column(DateTime(timezone=True), server_default=func.now())

    # — Campos para soft-delete —
    is_voided    = Column(Boolean, default=False, nullable=False)
    void_reason  = Column(String(256), nullable=True)
    voided_at    = Column(DateTime(timezone=True), nullable=True)
