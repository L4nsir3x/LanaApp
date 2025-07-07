from typing import List, Optional
from sqlalchemy.orm import Session
from datetime import datetime

from Lana_App.models.transaction  import Transaction
from Lana_App.schemas.transaction import TransactionCreate

def get_transaction(db: Session, transaction_id: int) -> Optional[Transaction]:
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()

def get_transactions(db: Session, skip: int = 0, limit: int = 100) -> List[Transaction]:
    return db.query(Transaction).offset(skip).limit(limit).all()

def create_transaction(db: Session, tx_in: TransactionCreate) -> Transaction:
    tx = Transaction(**tx_in.dict())
    db.add(tx)
    db.commit()
    db.refresh(tx)
    return tx

def cancel_transaction(db: Session, transaction_id: int, reason: str) -> Optional[Transaction]:
    tx = get_transaction(db, transaction_id)
    if not tx:
        return None
    tx.is_voided   = True
    tx.void_reason = reason
    tx.voided_at   = datetime.utcnow()
    db.commit()
    db.refresh(tx)
    return tx
