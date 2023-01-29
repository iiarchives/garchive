# Copyright 2022 iiPython

# Modules
import os
import json
from garchive import app
from flask import render_template, abort, send_from_directory

# Configuration
root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
season_folder = os.path.join(root, "seasons")
static_folder = os.path.join(root, "garchive/static")

# Routes
@app.route("/")
def route_home() -> None:
    return render_template(
        "home.html"
    ), 200

@app.route("/seasons")
def route_index() -> None:
    seasons = []
    for s in os.listdir(season_folder):
        with open(os.path.join(season_folder, s), "r") as fh:
            data = json.loads(fh.read())

        data["id"] = s.removesuffix(".json")
        seasons.append(data)

    return render_template(
        "seasons.html",
        seasons = sorted(seasons, key = lambda s: s["id"], reverse = True)
    ), 200

@app.route("/seasons/<string:sid>")
def route_details(sid: str) -> None:
    season_path = os.path.join(season_folder, f"{sid}.json")
    if not os.path.isfile(season_path):
        return abort(404)

    # Load season information
    with open(season_path, "r") as fh:
        data = json.loads(fh.read())

    return render_template(
        "details.html",
        data = data
    ), 200

@app.route("/~/<path:path>")
def route_static_file(path: str) -> None:
    return send_from_directory(static_folder, path)
