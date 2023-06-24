# Copyright 2023 iiPython

# Modules
import os
import uvicorn

# Launch
if __name__ == "__main__":
    uvicorn.run(
        "garchive:app",
        host = os.getenv("HOST", "0.0.0.0"),
        port = os.getenv("PORT", 8080),
        reload = True
    )
