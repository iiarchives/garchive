# Copyright 2023 iiPython

# Modules
import logging
from functools import wraps
from types import FunctionType

from blacksheep import Response
from blacksheep.server.responses import json

# Handle status related exceptions
def protected() -> FunctionType:
    def decorator(next):
        @wraps(next)
        async def wrapped(*args, **kwargs) -> Response:
            try:
                return json({
                    "success": True,
                    "data": await next(*args, **kwargs)
                })

            except Exception as e:
                logging.critical(e, exc_info = True)

            return json({"success": False, "data": {}}, status = 500)

        return wrapped

    return decorator
