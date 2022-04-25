import sys
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

sys.path.append("..")

from application import crud
from domain import models, schemas
from infrastructure.database import SessionLocal, engine
from infrastructure import fastapi_simple_security


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


depen = [Depends(fastapi_simple_security.api_key_security)]
emp = schemas.Empleado


@app.get("/empleados/", response_model=list[emp], dependencies=depen)
async def read_empleados(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    empleados = crud.get_empleados(db, skip=skip, limit=limit)

    return empleados


@app.get("/empleados/{empleado_id}", response_model=emp, dependencies=depen)
async def read_empleado(empleado_id: int, db: Session = Depends(get_db)):

    db_empleado = crud.get_empleado(db, empleado_id=empleado_id)

    if db_empleado is None:
        raise HTTPException(status_code=404, detail="No se encontro el Empleado")

    return db_empleado


@app.get("/empleados/{uuid_empleado}", response_model=emp, dependencies=depen)
async def read_empleado_uuid(uuid_empleado: str, db: Session = Depends(get_db)):

    db_empleado = crud.get_empleado_by_uuid(db, uuid_empleado)

    if db_empleado is None:
        raise HTTPException(status_code=404, detail="No se encontro el Empleado por el uuid")

    return db_empleado


@app.post("/empleados/", response_model=emp, dependencies=depen)
async def create_empleado(empleado: emp, db: Session = Depends(get_db)):

    db_empleado = crud.get_empleado_by_uuid(db, uuid=empleado.uuid)

    if db_empleado:
        raise HTTPException(status_code=400, detail="Empleado ya esta Registrado")

    return crud.create_empleado(db=db, empleado=dict(empleado))


@app.put("/empleados/{empleado_id}", dependencies=depen)
async def update_empleado(empleado_id: int, empleado: emp, db: Session = Depends(get_db)):

    db_empleado = crud.get_empleado(db, empleado_id=empleado_id)

    if db_empleado is None:
        raise HTTPException(status_code=404, detail="No se encontro el Empleado")

    try:
        crud.update_empleado(db=db,empleado_id=empleado_id,
                                empleado=dict(empleado))
        response = {"mensaje": "Se actualizo el empleado satisfactoriamente!",
                    "data": dict(empleado)}
    except:
        response = {"mensaje": "Error al actualizar el empleado"}
    
    return response


@app.delete("/empleados/{empleado_id}", dependencies=depen)
async def delete_empledo(empleado_id: int, db: Session = Depends(get_db)):

    try:
        crud.delete_empleado(db=db, empleado_id=empleado_id)
        response = {"mensaje": "Empleado ha sido eliminado exitosamente!"}
    except:
        response = {"mensaje": "No se pudo eliminar el Empleado!"}

    return response
