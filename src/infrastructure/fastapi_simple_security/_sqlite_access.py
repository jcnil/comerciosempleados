import sqlite3,os,uuid,threading
from datetime import datetime, timedelta
from typing import List, Tuple, Optional


class SQLiteAccess:
    def __init__(self):
        try:
            self.db_location = os.environ["FASTAPI_SIMPLE_SECURITY_DB_LOCATION"]
        except KeyError:
            self.db_location = "db/db.sqlite3"

        try:
            self.expiration_limit = int(
                os.environ["FAST_API_SIMPLE_SECURITY_AUTOMATIC_EXPIRATION"]
            )
        except KeyError:
            self.expiration_limit = 15

        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_location) as connection:
            c = connection.cursor()
            c.execute(
                """
                SELECT id,
                       uuid,
                       nombre,
                       activo,
                       email_contacto,
                       telefono_contacto,
                       api_key,
                       fecha_creacion
                                     FROM main_comercio
                """
            )
            connection.commit()

    def create_key(self, never_expire) -> str:
        api_key = str(uuid.uuid4())

        with sqlite3.connect(self.db_location) as connection:
            c = connection.cursor()
            c.execute(
                """
                INSERT INTO main_comercio
                (uuid, nombre, activo, email_contacto, telefono_contacto, api_key, fecha_creacion)
                    VALUES(?, ?, ?, ?, ?, ?, datetime('now'));
            """,
                (
                    str(uuid.uuid4()),
                    'Otro Comercio',
                    True,
                    '',
                    '',
                    api_key
                ),
            )
            connection.commit()

        return api_key

    def renew_key(self, api_key: str, new_expiration_date: str) -> Optional[str]:
        with sqlite3.connect(self.db_location) as connection:
            c = connection.cursor()

            c.execute(
                """
            SELECT id,
                       uuid,
                       nombre,
                       activo,
                       email_contacto,
                       telefono_contacto,
                       api_key,
                       fecha_creacion
                                     FROM main_comercio
            WHERE api_key = ?""",
                (api_key,),
            )

            response = c.fetchone()

            if not response:
                return "API key not found"

            response_lines = []

            if response[0] == 0:
                response_lines.append(
                    "This API key was revoked and has been reactivated."
                )

            if (not response[3]) and (
                datetime.fromisoformat(response[2]) < datetime.utcnow()
            ):
                response_lines.append("This API key was expired and is now renewed.")

            if not new_expiration_date:
                parsed_expiration_date = (
                    datetime.utcnow() + timedelta(days=self.expiration_limit)
                ).isoformat(timespec="seconds")
            else:
                try:
                    parsed_expiration_date = datetime.fromisoformat(
                        new_expiration_date
                    ).isoformat(timespec="seconds")
                except ValueError:
                    return (
                        "The expiration date could not be parsed. Please use ISO 8601."
                    )

            c.execute(
                """
            UPDATE main_comercio
            SET activo = 1
            WHERE api_key = ?
            """,
                (
                    api_key,
                ),
            )

            connection.commit()

            return "Se actualizo la key en el registro"

    def revoke_key(self, api_key: str):
        with sqlite3.connect(self.db_location) as connection:
            c = connection.cursor()

            c.execute(
                """
            UPDATE main_comercio
            SET activo = 0
            WHERE api_key = ?
            """,
                (api_key,),
            )

            connection.commit()

    def check_key(self, api_key: str) -> bool:

        with sqlite3.connect(self.db_location) as connection:
            c = connection.cursor()

            c.execute(
                """
            SELECT id,
                       uuid,
                       nombre,
                       activo,
                       email_contacto,
                       telefono_contacto,
                       api_key,
                       fecha_creacion
                                     FROM main_comercio
            WHERE api_key = ?""",
                (api_key,),
            )

            response = c.fetchone()

            if (
                # Cannot fetch a row
                not response
                # Inactive
                or response[0] != 1
                # Expired key
                or (
                    (not response[3])
                    and (datetime.fromisoformat(response[2]) < datetime.utcnow())
                )
            ):
                # The key is not valid
                return False
            else:

                return True

sqlite_access = SQLiteAccess()
