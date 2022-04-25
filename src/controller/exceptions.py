class BaseError(Exception):
    rc = -1000
    msg = "Error"


class NoEmpleadoError(BaseError):
    rc = -1001
    msg = "Please enter a valid id"


class InvalidEmpleadoError(BaseError):
    rc = -1002
    msg = "Invalid id"


class DuplicatedPinError(BaseError):
    rc = -1003
    msg = "Duplicated PIN"


class IncompleteDataError(BaseError):
    rc = -1004
    msg = "Incomplete data"
