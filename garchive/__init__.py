# Copyright 2022 iiPython

# Modules
import os
from flask import Flask

# Initialization
app = Flask(
    "GArchive",
    template_folder = os.path.join(os.path.dirname(__file__), "templates")
)

# Routes
from .routes import *
