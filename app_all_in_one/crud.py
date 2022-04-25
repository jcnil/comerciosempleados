from sqlalchemy.orm import Session
import models
import schemas


def get_empleado(db: Session, empleado_id: int):
    return db.query(models.Empleado).filter(models.Empleado.id == empleado_id).first()


def get_empleado_by_uuid(db: Session, uuid: str):
    return db.query(models.Empleado).filter(models.Empleado.uuid == uuid).first()


def get_empleados(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Empleado).offset(skip).limit(limit).all()


def create_empleado(db: Session, empleado: schemas.Empleado):
    db_empleado = models.Empleado(nombre=empleado['nombre'],
                                  apellidos=empleado['apellidos'],
                                  pin=empleado['pin'],
                                  comercio_id=empleado['comercio_id'])
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado


def update_empleado(db: Session, empleado_id: int, empleado: schemas.Empleado):
    data = {"nombre":empleado['nombre'],
            "apellidos":empleado['apellidos'],
            "pin":empleado['pin']}
    db.query(models.Empleado).filter(models.Empleado.id == empleado_id).update(data)
    db.commit()
    return data

def delete_empleado(db: Session, empleado_id: int):
    db.query(models.Empleado).filter(models.Empleado.id == empleado_id).delete()
    db.commit()
    return {"Response":200}