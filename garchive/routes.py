# Copyright 2022 iiPython

# Modules
import os
import json
from garchive import app, root, view
from blacksheep.server.responses import not_found

# Configuration
season_folder = os.path.join(root, "seasons")

# Routes
@app.route("/")
async def route_home() -> None:
    return await view("home", {})

@app.route("/seasons")
async def route_seasons() -> None:
    seasons = []
    for s in os.listdir(season_folder):
        with open(os.path.join(season_folder, s), "r") as fh:
            data = json.loads(fh.read())

        data["id"] = s.removesuffix(".json")
        seasons.append(data)

    return await view(
        "seasons",
        {"seasons": sorted(seasons, key = lambda s: s["id"], reverse = True)}
    )

@app.route("/seasons/{sid}")
async def route_details(sid: str) -> None:
    season_path = os.path.join(season_folder, f"{sid}.json")
    if not os.path.isfile(season_path):
        return not_found("No such season exists.")

    # Load season information
    with open(season_path, "r") as fh:
        data = json.loads(fh.read())

    return await view(
        "details",
        {"data": data}
    )

@app.route("/faq")
async def route_faq() -> None:
    return await view("faq", {})

@app.route("/contacts")
async def route_contacts() -> None:
    return await view("contacts", {})
