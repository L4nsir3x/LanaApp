from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from Lana_App.database import Base  # Asegúrate de que esta ruta sea correcta

class FixedPayment(Base):
    __tablename__ = "pagos_fijos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    monto = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)
    usuario_id = Column(Integer, nullable=False)  # ✅ Puedes agregar ForeignKey si ya tienes la tabla usuarios
    # usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)  # ← Usa esto si ya creaste la tabla usuarios
