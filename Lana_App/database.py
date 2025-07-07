from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Aquí defines la URL de tu base de datos
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Usa SQLite local

# Crear el engine de SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para todos los modelos (User, PagosFijos, etc.)
Base = declarative_base()

# Dependencia que se usará con Depends()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
