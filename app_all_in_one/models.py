from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

from datetime import datetime
import uuid as _uuid

class Comercio(Base):
    __tablename__ = "main_comercio"

    id = Column(Integer, primary_key=True)
    uuid = Column(String, default=str(_uuid.uuid4()))
    nombre = Column(String)
    activo = Column(Boolean, default=True)
    email_contacto = Column(String, unique=True)
    telefono_contacto = Column(String, default=None)
    api_key = Column(String, default=_uuid.uuid4)
    fecha_creacion = Column(DateTime, default=datetime.now)

    empleados = relationship("Empleado", back_populates="pertenece")


class Empleado(Base):
    __tablename__ = "main_empleado"

    id = Column(Integer, primary_key=True)
    uuid = Column(String, default=str(_uuid.uuid4()))
    nombre = Column(String)
    apellidos= Column(String)
    pin= Column(String)
    comercio_id = Column(Integer, ForeignKey("main_comercio.id"))
    fecha_creacion = Column(DateTime, default=datetime.now)
    activo= Column(Boolean, default=True)

    pertenece = relationship("Comercio", back_populates="empleados")

