# Copyright 2022-2023 iiPython

# Modules
import os
import sys
from jinja2 import FileSystemLoader
from blacksheep import Application
from blacksheep.server.templating import use_templates

# Initialization
root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
app = Application(debug = "--reload" in sys.argv)
app.serve_files(os.path.join(root, "garchive/static"), root_path = "~", extensions = (".css", ".ico", ".mp3", ".png", ".zip"))
view = use_templates(
    app,
    loader = FileSystemLoader(os.path.dirname(__file__)),
    enable_async = True
)

# Clean up HTML output
app.jinja_environment.lstrip_blocks = True

# Start username identification
from .identity import start_loop, match_ip
start_loop()

# Routes
from .routes import *
