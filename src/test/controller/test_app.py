from fastapi.testclient import TestClient
import uuid as _uuid
from datetime import datetime
from controller.main import app


client = TestClient(app)


def test_read_empleados():
    response = client.get("/empleados/")
    assert response.status_code == 200


def test_read_empleado():
    response = client.get("/empleados/1")
    assert response.status_code == 200
    assert response.json() == {"nombre": "Tony",
                               "apellidos": "Stark",
                               "pin": "123456",
                               "id": 1,
                               "uuid": "bccee0304bde42a5a79c9dcbbad2c645",
                               "comercio_id": 1,
                               "fecha_creacion": "2021-07-23T22:04:08.947309",
                               "activo": True}


def test_read_empleado_uuid():
    response = client.get("/empleados?uuid=0f34892834634e2db677b9acc8f89438")
    assert response.status_code == 200
    assert response.json() == {"nombre": "Steve",
                               "apellidos": "Rogers",
                               "pin": "000000",
                               "id": 2,
                               "uuid": "0f34892834634e2db677b9acc8f89438",
                               "comercio_id": 1,
                               "fecha_creacion": "2021-07-23T22:05:08.585083",
                               "activo": True}


def test_create_empledo():
    data = {"nombre": "Peter",
            "apellidos": "Williams",
            "pin": "087695",
            "id": 10,
            "uuid": str(_uuid.uuid4()),
            "comercio_id": 1,
            "fecha_creacion": datetime.now(),
            "activo": True}

    response = client.post("/empleados/", data=data)
    assert response.status_code == 200
    assert response.json() == data


def test_update_empledo():
    data = {"nombre": "Peter",
            "apellidos": "Williams",
            "pin": "087695"}
    response = client.put("/empleados/1", data=data)
    assert response.status_code == 200


def test_delete_empledo():
    response = client.delete("/empleados/4")
    assert response.status_code == 200
