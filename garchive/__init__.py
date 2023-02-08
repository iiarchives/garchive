# Copyright 2022-2023 iiPython

# Modules
import os
import sys
from jinja2 import FileSystemLoader
from blacksheep import Application
from blacksheep.server.templating import use_templates

from .static import serve_files_dynamic

# Initialization
root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
app = Application(debug = "--reload" in sys.argv)
serve_files_dynamic(
    app.router,
    app.files_handler,
    os.path.join(root, "garchive/static"),
    root_path = "~",
    extensions = (".css", ".ico", ".mp3", ".png", ".zip"),
    discovery = False,
    cache_time = 10800,
    index_document = "index.html",
    fallback_document = None
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

# Start username identification
from .identity import start_loop, match_ip  # noqa: all
start_loop()

# Routes
from .routes import *  # noqa: all
