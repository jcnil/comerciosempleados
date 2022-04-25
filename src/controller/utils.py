from fastapi import HTTPException
from controller.exceptions import BaseError


def custom_exception_handler(exc, context):

    if isinstance(exc, BaseError):
        response = HTTPException(status_code=exc.rc, detail=exc.msg)
    else:
        print(exc.__class__)
        old_response = HTTPException(exc, context)
        response = old_response
        # Now add the HTTP status code to the response.
        if response is not None:
            response.data['rc'] = response.status_code * -1
            response.data['msg'] = response.data['detail']
            del response.data['detail']

    if response is None:
        response = HTTPException(status_code=-654, detail=str(exc))

    return response
