from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from datetime import datetime
from sqlalchemy.orm import Session

from Lana_App.database            import get_db
from Lana_App.schemas.transaction import Transaction, TransactionCreate
from Lana_App.crud.transaction    import (
    get_transaction,
    get_transactions,
    create_transaction,
    cancel_transaction  # antes delete_transaction
)

router = APIRouter(prefix="/transacciones", tags=["Transacciones"])

@router.post("/", response_model=Transaction, status_code=status.HTTP_201_CREATED)
def create(tx_in: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(db, tx_in)

@router.get("/{tx_id}", response_model=Transaction)
def read(tx_id: int, db: Session = Depends(get_db)):
    tx = get_transaction(db, tx_id)
    if not tx:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    return tx

@router.get("/", response_model=List[Transaction])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_transactions(db, skip, limit)

@router.delete(
    "/{tx_id}",
    response_model=Transaction,
    status_code=status.HTTP_200_OK,
    summary="Cancela (soft-delete) una transacción",
    description="Marca la transacción como anulada, sin borrarla de BD."
)
def cancel(
    tx_id: int,
    reason: str = Query(..., description="Motivo de la cancelación"),
    db: Session = Depends(get_db)
):
    tx = cancel_transaction(db, tx_id, reason)
    if not tx:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    return tx
