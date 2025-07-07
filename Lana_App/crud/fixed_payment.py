from sqlalchemy.orm import Session
from Lana_App.models.fixed_payment import FixedPayment
from Lana_App.schemas.fixed_payment import FixedPaymentCreate

def create_fixed_payment(db: Session, payment: FixedPaymentCreate):
    db_payment = FixedPayment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def get_fixed_payments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(FixedPayment).offset(skip).limit(limit).all()
