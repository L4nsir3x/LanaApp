from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Lana_App.database import get_db
from Lana_App.schemas.fixed_payment import FixedPaymentCreate, FixedPaymentOut
from Lana_App.crud import fixed_payment
from Lana_App.models.fixed_payment import FixedPayment

router = APIRouter(
    prefix="/pagos-fijos",
    tags=["Pagos Fijos"]
)

@router.post("/", response_model=FixedPaymentOut)
def create(payment: FixedPaymentCreate, db: Session = Depends(get_db)):
    return fixed_payment.create_fixed_payment(db, payment)

@router.get("/{usuario_id}", response_model=list[FixedPaymentOut])
def read(usuario_id: int, db: Session = Depends(get_db)):
    return fixed_payment.get_fixed_payments(db, usuario_id)

@router.delete("/{payment_id}")
def delete_fixed_payment(payment_id: int, db: Session = Depends(get_db)):
    pago = db.query(FixedPayment).filter(FixedPayment.id == payment_id).first()
    if not pago:
        raise HTTPException(status_code=404, detail="Pago fijo no encontrado")
    db.delete(pago)
    db.commit()
    return {"mensaje": "Pago fijo eliminado"}
