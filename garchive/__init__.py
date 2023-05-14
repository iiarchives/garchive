# Copyright 2022-2023 iiPython

# Modules
import os
import sys
import asyncio
from jinja2 import FileSystemLoader
from blacksheep import Application
from blacksheep.server.templating import use_templates

from .logging import logger
from .minecraft import fetch_status, ServerStatus
from .utils import preload_seasons, convert_png_to_webp

# Initialization
root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
app = Application(debug = "--reload" in sys.argv)
app.serve_files(
    os.path.join(root, "garchive/static"),
    root_path = "~",
    extensions = (".css", ".js", ".mp3", ".ico", ".png", ".svg", ".webp", ".zip")
)

# Jinja2 setup
view = use_templates(
    app,
    loader = FileSystemLoader([
        os.path.join(os.path.dirname(__file__), "templates"),
        os.path.join(os.path.dirname(__file__), "static")
    ]),
    enable_async = True
)

# Clean up HTML output
app.jinja_environment.lstrip_blocks = True

# Convert PNGs to webp
seasons_directory = os.path.join(root, "garchive/static/seasons")
logger.info("Converting PNGs to Webp ...")
# convert_png_to_webp(seasons_directory)
logger.info("All PNGs successfully converted to Webp!")

# Load seasons into RAM
logger.info("Loading seasons into RAM ...")
# seasons = preload_seasons(seasons_directory)
seasons = []
logger.info(f"Preloaded {len(seasons)} seasons into RAM!")

# Launch status checks
if os.getenv("GC_ADDRESS"):
    server_status = ServerStatus()

    # Start background checks
    async def conf_bgtasks(app):
        asyncio.get_event_loop().create_task(fetch_status(app, server_status))

    app.on_start += conf_bgtasks

    # Handle routing
    async def route_status() -> dict:
        return server_status.to_json()

    app.router.add_get("/api/status", route_status)

# Routes
from .routes import (api, public)  # noqa: all
