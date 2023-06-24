# Copyright 2023 iiPython

# Modules
import tomllib
import pathlib
from typing import Any

# Initialization
config_file = pathlib.Path(__file__).parents[1] / "config.toml"
if not config_file.exists():
    exit("Missing config.toml in garchive root directory.")

# Load configuration
class Configuration(object):
    def __init__(self) -> None:
        self.obj = {}
        with open(config_file, "r") as fh:
            self.obj = tomllib.loads(fh.read())

    def __getitem__(self, index: str) -> Any:
        o = self.obj
        for k in index.split("."):
            o = o[k]

        return o

config = Configuration()
