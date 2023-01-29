# Copyright 2022 iiPython

# Modules
import os
import re
import sys
import gzip
import shutil
import tarfile

# Initialization
if not sys.argv[1:]:
    exit("usage: log_compiler.py <log_directory>")

log_directory = sys.argv[1]
if not os.path.isdir(log_directory):
    exit("log directory does not exist")

os.chdir(log_directory)
if os.path.isfile("latest.log"):
    os.remove("latest.log")
    print("[+] Removed latest.log")

# Extract all log files
for file in os.listdir():
    if not file.endswith(".log.gz"):
        continue

    log_id = file.split(".")[0]
    with gzip.open(file, "rb") as gzin:
        with open(f"{log_id}.log", "wb") as out:
            shutil.copyfileobj(gzin, out)

    print(f"[+] Extracted {file} to {log_id}.log")
    os.remove(file)
    print(f"[+] Removed {file}")

# Scrub for ip addresses
for file in os.listdir():
    if not file.endswith(".log"):  # Nothing else should exist, but better safe than sorry
        continue

    with open(file, "r") as fh:
        text_content = fh.read()

    for address in re.findall(re.compile(r"((\d{1,3}\.){3}\d{1,3})"), text_content):
        text_content = text_content.replace(address[0], "xx.xx.xx.xx")

    with open(file, "w") as fh:
        fh.write(text_content)

    print(f"[+] Filtered IP addresses from {file}")

# Archive into a large log file
with tarfile.open("logs.tgz", "w:gz") as tar:
    [tar.add(file) for file in os.listdir()]

print("[+] Created logs.tgz")
