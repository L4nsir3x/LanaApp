from fastapi import FastAPI
from Lana_App.routers import fixed_payment
from Lana_App.database import engine, Base  # ✅ Importar la BD

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registrar el router de pagos fijos
app.include_router(
    fixed_payment.router,
    prefix="/pagos-fijos",
    tags=["Pagos Fijos"]
)
