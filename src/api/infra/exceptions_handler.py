from fastapi import Request
from fastapi.responses import JSONResponse

from api.domain.exceptions import IntegrityException


async def integrity_exception_handler(request : Request , exception : IntegrityException):
    return JSONResponse(
        content={"err" : exception.message},
        status_code=exception.code
    )
