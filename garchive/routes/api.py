# Copyright 2023 iiPython

# Modules
from blacksheep.server.responses import not_found

from .. import app, seasons

# Routes
@app.route("/api/seasons")
async def route_api_seasons() -> dict:
    return {"code": 200, "data": seasons}

@app.route("/api/seasons/<string:ident>")
async def route_api_season(ident: str, field: str = None) -> dict:
    season = seasons.get(ident)
    if season is None:
        return not_found({"code": 404, "message": "Season not found."})

    return {
        "code": 200,
        "data": season if field is None else season.get(field)
    }
