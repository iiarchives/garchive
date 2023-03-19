# Copyright 2023 iiPython

# Modules
from blacksheep.server.responses import not_found

from .. import app, seasons

# Routes
@app.route("/api/seasons")
async def route_api_seasons(id: str = None, field: str = None) -> dict:
    data = seasons
    if id is not None:
        data = seasons.get(id)
        if data is None:
            return not_found({"code": 404, "message": "Season not found."})

        data = data if field is None else data.get(field)

    return {"code": 200, "data": data}
