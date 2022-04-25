from datetime import datetime
from pydantic import BaseModel, Field, ValidationError
from typing import Optional

import uuid as _uuid


class Comercio(BaseModel):
    id: Optional[int]
    uuid: Optional[str] = str(_uuid.uuid4())
    activo: Optional[bool] = True
    nombre: str
    email_contacto: Optional[str] = None
    telefono_contacto: Optional[str] = None
    api_key: Optional[str] = str(_uuid.uuid4())
    fecha_creacion: Optional[datetime] = datetime.now()

    class Config:
        orm_mode = True


class Empleado(BaseModel):
    id: Optional[int]
    uuid: Optional[str] = str(_uuid.uuid4())
    nombre: str
    apellidos: str
    pin: str
    comercio_id: int
    fecha_creacion: Optional[datetime] = datetime.now()
    activo: Optional[bool] = True

    class Config:
        orm_mode = True

