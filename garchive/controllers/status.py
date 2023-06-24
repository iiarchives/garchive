# Copyright 2023 iiPython

# Modules
from mcstatus import JavaServer
from blacksheep.server.controllers import ApiController, get

from .common import protected
from ..config import config

# Connect to server
try:
    server = JavaServer.lookup(config["server.address"])

except (TypeError, ValueError) as e:
    exit(e)

# Main status class
class Status(ApiController):
    @get()
    @protected()
    async def get_status(self) -> dict:
        """Returns the current server status"""
        return (await server.async_status()).raw
