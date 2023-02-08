# Copyright 2023 iiPython

# Modules
import os
import re
import gzip
import json
import atexit
import logging
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.schedulers.background import BackgroundScheduler

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

# Initialization
GC_SEASON_PATH  = os.getenv("GA_SEASON_PATH", "")
DISABLE_SCHED   = os.getenv("GA_DISABLE_IPCHECK", "").lower() in ["true", "1"]
if (not DISABLE_SCHED) and (not os.path.isdir(GC_SEASON_PATH)):
    logger.warn("GA_SEASON_PATH does not exist and GA_DISABLE_IPCHECK is False!")
    logger.warn("GArchive is falling back to GA_DISABLE_IPCHECK=1!")
    DISABLE_SCHED = True

GC_LOG_PATH = os.path.join(GC_SEASON_PATH, "logs")
DATA_PATH   = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
if not os.path.isdir(DATA_PATH):
    os.mkdir(DATA_PATH)

IP_ASSOC_PATH = os.path.join(DATA_PATH, "assocs.json")

# Log collectors
ip_regex = re.compile(r"(\w*)\[\/((\d+\.?){4})")
def parse_log(log: str) -> dict:
    lines = log.splitlines()
    lines.reverse()  # call .reverse() so we use the latest IPs
    return {m[1]: m[0] for m in re.findall(ip_regex, "\n".join(lines))}

def update_ip_assocs() -> None:
    logger.info("GArchive is updating IP associations ...")
    if not os.path.isfile(IP_ASSOC_PATH):
        data = {}

    else:
        with open(IP_ASSOC_PATH, "r") as fh:
            data = json.loads(fh.read())

    # Calculate what gzs to load
    files, assocs = os.listdir(GC_LOG_PATH), {}
    if "skip" in data:
        files = files[data["skip"]:]

    for file in sorted(files):
        if not file.endswith(".gz"):
            continue

        with open(os.path.join(GC_LOG_PATH, file), "rb") as fh:
            logfile = gzip.GzipFile(fileobj = fh)
            assocs = assocs | parse_log(logfile.read().decode("utf8"))

    data["skip"] = len(files) - 1
    if "assocs" in data:
        data["assocs"] = data["assocs"] | assocs

    else:
        data["assocs"] = assocs

    with open(IP_ASSOC_PATH, "w+") as fh:
        data = fh.write(json.dumps(data))

def match_ip(ip: str) -> None:
    if ip == "127.0.0.1":
        return "Dev"  # Allow downloading season ZIPs when developing

    # Load IP data and match it
    if not os.path.isfile(IP_ASSOC_PATH):
        return None

    with open(IP_ASSOC_PATH, "r") as fh:
        data = json.loads(fh.read())

    return data.get("assocs", {}).get(ip)

# Loop handler
def start_loop() -> None:
    if DISABLE_SCHED:
        return

    # Start scheduler
    sched = BackgroundScheduler()
    sched.add_job(update_ip_assocs, IntervalTrigger(seconds = 5))
    sched.start()

    # Ensure scheduler stops at program exit
    atexit.register(lambda: sched.shutdown(wait = False))
