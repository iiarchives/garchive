# Copyright 2023 iiPython

# Modules
import os
import asyncio
from time import time
from mcstatus import JavaServer
from blacksheep import Application

from .logging import logger

# Initialization
address = os.getenv("GC_ADDRESS", "")
if address.strip():
    server_instance = JavaServer.lookup(address)

# Datastore
class ServerStatus(object):
    def __init__(self) -> None:
        self.members = []
        self.ping = 0

    def to_json(self) -> None:
        return {"members": self.members, "ping": self.ping, "timestamp": round(time() * 1000)}

# Main handler
async def fetch_status(app: Application, serverstats: ServerStatus) -> None:
    while True:

        # Fetch information
        try:
            status = server_instance.status()

        except Exception as e:
            logger.error("Failed fetching server stats!")
            return logger.error(e)

        # Update app service
        serverstats.members = [
            {"name": u.name, "id": u.id} for u in status.players.sample or []
        ]
        serverstats.ping = round(status.latency, 2)

        # Update every 15 seconds
        await asyncio.sleep(15)
