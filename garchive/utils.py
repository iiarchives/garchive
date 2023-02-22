# Copyright 2023 iiPython

# Modules
import os
import json
from PIL import Image
from typing import Dict, Any

from .logging import logger

# Utilities
def convert_png_to_webp(directory: str) -> None:
    for path, _, files in os.walk(directory):
        for file in files:
            if file.split(".")[-1] != "png":
                continue

            webp_path = os.path.join(path, file.replace(".png", ".webp"))
            if os.path.isfile(webp_path):
                continue

            # Convert file
            try:
                image = Image.open(os.path.join(path, file)).convert("RGB")
                image.save(webp_path, "webp")
                logger.info(f"[Webp]: SUCCESSFULLY converted {file}!")

            except Exception as err:
                logger.error("[Webp]: FAILED to convert {file}! Traceback following:")
                raise err

def preload_seasons(directory: str) -> Dict[str, Dict[str, Any]]:
    directory, seasons = os.path.abspath(directory), {}
    for sid in os.listdir(directory):
        sdir = os.path.join(directory, sid)
        json_file = os.path.join(sdir, "season.json")
        with open(json_file, "r") as fh:
            season = json.loads(fh.read())

        seasons[sid] = season | {
            "id": sid,
            "download": os.path.isfile(os.path.join(sdir, "download.zip")),
            "gallery": [
                x for x in os.listdir(os.path.join(sdir, "gallery"))
                if x.endswith(".png")
            ]
        }

    return seasons
