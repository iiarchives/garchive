# Copyright 2022 iiPython

# Modules
import os
import sys
from garchive import app

# Launch app
if __name__ == "__main__":
    app.run(
        host = "0.0.0.0",
        port = os.getenv("PORT", 8080),
        debug = "--debug" in sys.argv
    )
