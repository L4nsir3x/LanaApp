from pydantic import BaseModel
from datetime import date

class FixedPaymentBase(BaseModel):
    nombre: str
    monto: float
    fecha: date

class FixedPaymentCreate(FixedPaymentBase):
    usuario_id: int

class FixedPaymentOut(FixedPaymentBase):
    id: int

    class Config:
        from_attributes = True  # ✅ Cambio para Pydantic v2
