# Copyright 2022-2023 iiPython

# Modules
import os
import json
from garchive import app, root, view
from blacksheep.server.responses import not_found

# Configuration
season_folder = os.path.join(root, "garchive/static/seasons")

# Routes
@app.route("/")
async def route_home() -> None:
    return await view("templates/home", {})

@app.route("/seasons")
async def route_seasons() -> None:
    seasons = []
    for s in os.listdir(season_folder):
        with open(os.path.join(season_folder, s, "season.json"), "r") as fh:
            data = json.loads(fh.read())

        data["id"] = s
        seasons.append(data)

    return await view(
        "templates/seasons",
        {"seasons": sorted(seasons, key = lambda s: s["start"] or "")}
    )

@app.route("/seasons/{sid}")
async def route_details(sid: str) -> None:
    season_path = os.path.join(season_folder, sid, "season.json")
    if not os.path.isfile(season_path):
        return not_found("No such season exists.")

    # Load season information
    with open(season_path, "r") as fh:
        data = json.loads(fh.read())
        data["download"] = os.path.isfile(os.path.join(season_folder, sid, "download.zip"))
        data["id"] = sid
        data["gallery"] = os.listdir(os.path.join(season_folder, sid, "gallery"))

    return await view(
        f"static/seasons/{sid}/about",
        {"data": data}
    )
