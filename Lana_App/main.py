from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Lana_App.database import engine, Base
from Lana_App.routers import (
    fixed_payment,
    transaction  # tu router de transacciones
)

app = FastAPI(
    title="API de tu Proyecto",
    version="1.0.0",
    description="Aquí van detalles de tu API"
)

# --- Middleware CORS (ajusta orígenes según necesites) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5000", "http://localhost:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Startup: crear BD/tablas antes de arrancar ---
@app.on_event("startup")
async def on_startup():
    # si usas SQLAlchemy sincronizado:
    Base.metadata.create_all(bind=engine)
    # si tienes alguna inicialización async, hazla aquí
    # p. ej. await some_async_setup()

# --- Montar routers ---
app.include_router(
    fixed_payment.router,
    prefix="/pagos-fijos",
    tags=["Pagos Fijos"]
)

app.include_router(
    transaction.router,
    prefix="/transacciones",
    tags=["Transacciones"]
)

# --- Root opcional ---
@app.get("/", tags=["Root"])
async def root():
    return {"mensaje": "Bienvenido a tu API"}

