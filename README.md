# REST API - Python - FastAPI (SOLID & Hexagonal Arch.)

REST API creada con Python, el framework web FlastAPI y SQLAlchemy ,con el protocolo HTTP, se replicaron las mismas peticiones que se tienen en el proyecto [comerciosempleados](https://github.com/alfaro28/comerciosempleados).

<hr/>


## Para Correger la aplicacion se debe:

1. Crear un virtualenv en mi caso use pyenv para crear un entorno virtual:

    `$ pyenv virtualenv 3.9.5  <nombre_ambiente>`

    Luego se activa el entorno virtual:

    `$ pyenv activate <nombre_ambiente>`

    y posteriormente se corre el paso 2, para mayor insformacion consultar la [pagina](https://realpython.com/intro-to-pyenv/)     

2. Instalar las librerias que estan en el archivo de requirements.txt ejecuntado el siguiente comando

   `$ pip3 install -r requirements.txt`

3. Luego a traves del shell se ingresa a la carpeta src, luego ingresas a la carpeta controller y se ejecuta el siguiente comando

   `$ uvicorn main:app --reload`

Para su informacion trate de estructurarla hexagonalmente sin embargo ahi cosas que no me funcionan como en la carpeta app, son el mismo proyecto lo unico es que en una esta estructurada de manera hexagonal y en la otra no solo FYI. De ser posible pruben las dos aplicaciones Por Favor.

Ahora, la API está escuchando en el puerto localhost 8000:

 - [http://localhost:8000/docs#/](http://localhost:8000/docs#/)


 ### Estructura del código

El árbol de directorios del código fuente se ve así:

```
.
src
├── application
│   ├── __init__.py
│   └── crud.py
├── controller
│   ├── exceptions.py
│   ├── main.py ---------------> API entry point
│   ├── utils.py
│   ├── __init__.py
├── domain
│   ├── __init__.py
│   ├── models.py
│   └── schemas.py
├── infrastructure
│   ├── __init__.py
│   ├── database.py
│   └── db
│   │   └── db.sqlite3
│   └── fastapi_simple_security
│       ├── _security_secret.py
│       ├── _sqlite_access.py
│       ├── security_api_key.py
│       └── __init__.py
├── test
│   ├── controller
│   │   ├── __init__.py
│   │   └── test_app.py
│   └── __init__.py
└── requirements.txt
```

## Pruebas

### Ejecutando pruebas

Las pruebas se han creado con pytest

## Solucion por

* José Nicolielly - - [jnicolielly](#)