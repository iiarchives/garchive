# Geesecraft Archives

A minecraft server hosted by the Geese, for the Geese.  
Geesecraft is a Minecraft server hosted by [iiPython](https://github.com/iiPythonx) about once per year (usually around summer) with a website to host archived season information, show screenshots, present modifications, and overall act as a central activity hub for the server.  

This activity hub is [garchive](https://github.com/iiPythonx/garchive), the repository you are currently viewing.

## Getting started

### Downloading

GArchive can be downloaded either via a ZIP file provided by GitHub, or by directly cloning the repository:
```sh
git clone git@github.com:iiPythonx/garchive  # If you use SSH to authentication with GH
git clone https://github.com/iiPythonx/garchive  # or if you prefer something simpler
```

Before doing anything else, it is recommended to install the requirements:
```sh
cd garchive

# If you're on windows, you should substitute python3 with py
python3 -m pip install -r reqs.txt
```

### Launching

For development, GArchive provides a `launch_debug.py` file that launches the site with one [uvicorn](https://www.uvicorn.org/) worker:
```sh
python3 launch_debug.py
```

### Environment

Please refer to [ENVIRONMENT.md](https://github.com/iiPythonx/garchive/blob/main/docs/ENVIRONMENT.md).

## Contributors

Most of the backend is maintained by [iiPython](https://github.com/iiPythonx).  
Meanwhile, [DmmD](https://github.com/DmmDGM) handles the entire frontend and templating system.

## Built with

GArchive uses the following libraries:
- [Uvicorn](https://www.uvicorn.org/) to host the web application alongside [gunicorn](https://gunicorn.org/).
- [Jinja2](https://jinja.palletsprojects.com/) to create and render our server-side templates.
- [Pillow](https://pillow.readthedocs.io/en/stable/) to convert PNGs to Webp for client-side performance gains.
- [MCStatus](https://github.com/Dinnerbone/mcstatus) to check our servers ping time and member list.
- [Blacksheep](https://github.com/Neoteroi/BlackSheep) to build the app using [Flask](https://flask.palletsprojects.com/)-like syntax.
