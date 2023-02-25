# Copyright 2022-2023 iiPython

# Modules
import time
from blacksheep import Request
from blacksheep.server.responses import not_found, see_other

from .. import app, view, seasons

# Routes
@app.route("/")
async def route_home() -> None:
    return await view("home", {})

@app.route("/api")
async def route_api_docs() -> None:
    return await view("api", {})

@app.route("/seasons")
async def route_seasons() -> None:
    return await view(
        "seasons",
        {
            "seasons": sorted(
                seasons.values(),
                key = lambda s: s["timestamp"] or time.time() * 1000,
                reverse = True
            )
        }
    )

@app.route("/seasons/{sid}")
async def route_details(request: Request, sid: str) -> None:
    if sid == "latest":
        return see_other(f"/seasons/{sorted(seasons.values(), key = lambda s: s['timestamp'] or 0, reverse = True)[0]['id']}")

    elif sid not in seasons:
        return not_found("Season not found.")

    # Render template
    return await view(
        "details.html",
        {
            "data": seasons[sid]
        }
    )

@app.route("/you-egged-up")
async def route_egged_up() -> None:
    return await view("abcdefgg", {})
