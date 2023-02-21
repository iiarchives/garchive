# Copyright 2023 iiPython

# Modules
import os
import uvicorn

# Launch GArchive
from garchive import app
uvicorn.run(
    app,
    host = "0.0.0.0",
    port = os.getenv("PORT", 8080)
)
