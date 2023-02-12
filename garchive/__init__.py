# Copyright 2022-2023 iiPython

# Modules
import os
import sys
import asyncio
from PIL import Image
from jinja2 import FileSystemLoader
from blacksheep import Application
from blacksheep.server.templating import use_templates

from .logging import logger
from .minecraft import fetch_status, ServerStatus

# Initialization
root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
app = Application(debug = "--reload" in sys.argv)
app.serve_files(
    os.path.join(root, "garchive/static"),
    root_path = "~",
    extensions = (".css", ".ico", ".mp3", ".png", ".zip", ".webp")
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
logger.info("Converting PNGs to Webp ...")
for path, _, files in os.walk(os.path.join(root, "garchive/static/seasons")):
    for file in files:
        if file.split(".")[-1] != "png":
            continue

        webp_path = os.path.join(path, file.replace(".png", ".webp"))
        if os.path.isfile(webp_path):
            continue

        # Convert file
        image = Image.open(os.path.join(path, file)).convert("RGB")
        image.save(webp_path, "webp")
        logger.info(f"[Webp]: {file}")

logger.info("All PNGs successfully converted to Webp!")

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

    app.router.add_get("/status", route_status)

# Routes
from .routes import *  # noqa: all
