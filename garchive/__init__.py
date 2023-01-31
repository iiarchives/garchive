# Copyright 2022 iiPython

# Modules
import os
import sys
from jinja2 import FileSystemLoader
from blacksheep import Application
from blacksheep.server.templating import use_templates

# Initialization
root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
app = Application(debug = "--reload" in sys.argv)
app.serve_files(os.path.join(root, "garchive/static"), root_path = "~")
view = use_templates(
    app,
    loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    enable_async = True
)

# Routes
from .routes import *
