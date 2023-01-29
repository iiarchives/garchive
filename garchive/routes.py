# Copyright 2022 iiPython

# Modules
import os
import json
from garchive import app
from flask import render_template, abort, send_from_directory

# Configuration
season_folder = os.path.abspath("seasons")

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
        d = json.loads(open(os.path.join(season_folder, s), "r").read())
        d["runtime"] = d["start"] + " - " + (d["end"] or "today")
        d["active"] = not bool(d["end"])
        d["id"] = s
        seasons.append(d)

    return render_template(
        "seasons.html",
        seasons = sorted(seasons, key = lambda s: s["end"] or "")
    ), 200

@app.route("/seasons/<string:sid>")
def route_details(sid: str) -> None:
    lseason_folder = os.path.join(season_folder, sid)
    if not os.path.isdir(lseason_folder):
        return abort(404)

    # Load season information
    with open(os.path.join(lseason_folder, "season.json"), "r") as fh:
        data = json.loads(fh.read())

    data["world_download"] = os.path.isfile(os.path.join(lseason_folder, "season.zip"))
    data["id"] = sid
    with open(os.path.join(lseason_folder, "whitelist.json"), "r") as fh:
        data["whitelist"] = json.loads(fh.read())

    return render_template(
        "details.html",
        data = data
    ), 200

@app.route("/seasons/<string:sid>/download")
def route_season_download(sid: str) -> None:
    return send_from_directory(season_folder, os.path.join(sid, "season.zip"), conditional = True)

@app.route("/seasons/<string:sid>/logs/download")
def route_season_logs_download(sid: str) -> None:
    return send_from_directory(season_folder, os.path.join(sid, "logs.tgz"), conditional = True)

@app.route("/~/<path:path>")
def route_static_file(path: str) -> None:
    return send_from_directory("garchive/static", path)
