from sqlalchemy import Column, Integer, String
from database import Base
from Lana_App.models import usuario  # 👈 Asegura que se importe


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
