# Copyright 2022-2023 iiPython

# Modules
import time
from blacksheep.server.responses import not_found, see_other

from .. import app, view, seasons

# Routes
@app.route("/")
async def route_home() -> None:
    return await view("home", {})

@app.route("/api")
async def route_api_docs() -> None:
    return await view("api", {})

@app.route("/archives")
async def route_archives() -> None:
    return await view("archives", {})

@app.route("/archives/{sid}")
async def route_season(sid: str) -> None:
    # if sid == "latest":
    #     return see_other(f"/seasons/{sorted(seasons.values(), key = lambda s: s['timestamp'] or 0, reverse = True)[0]['id']}")

    # elif sid not in seasons:
    #     return not_found("Season not found.")

    # Render template
    print(sid)
    return await view(
        f"/seasons/{sid}/index", {}
        # {
        #     "data": seasons[sid]
        # }
    )
