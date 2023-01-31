# Copyright 2023 iiPython

# Modules
import os
import sys
import uvicorn

# Debug env
if "--ipcheck" not in sys.argv:
    os.environ["GA_DISABLE_IPCHECK"] = "1"

# Launch GArchive
from garchive import app
uvicorn.run(
    app,
    host = "0.0.0.0",
    port = os.getenv("PORT", 8080)
)
