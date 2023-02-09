# Copyright 2023 iiPython

# Modules
import logging

# Logging (piggyback on uvicorn)
logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(message)s",
            "use_colors": None
        }
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        }
    },
    "loggers": {
        "garchive": {"handlers": ["default"], "level": "INFO", "propagate": False}
    },
})
logger = logging.getLogger("garchive")
