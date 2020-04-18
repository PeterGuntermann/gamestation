# gamestation
Just a simple game service.

# Notizen

+ Das Tutorial hier hilft: 
    - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
+ Axios-Tutorial:
    - https://www.youtube.com/watch?v=6LyagkoRWYA

## how to use
+ Enter the server via `ssh <user>@<host>`.
+ Move to the correct directory.
+ Install flask using `pip3 install -t <path> flask`.
+ Start the service with `python3 gamestation.py`

# Development
## Set up dev environment
+ Create a folder `venv`
+ Create the virtual environment: `python3 -m venv venv`
+ Activate the environment: `venv\Scripts\activate` (Windows 10)
+ Install packages: `pip install <package>`
    - `flask`
    - `python-dotenv`
    - `flask-wtf`

## Run dev server
### Using a PyCharm run config
+ `Alt + Shift + F10`
+ Edit configurations (`0`)
+ Add new configuration (`Alt + Insert`)
    - Name: as you wish (e.g. `flask dev server`)
    - Script path: `C:\<path_to_project>\venv\Scripts\flask.exe`
    - Parameters: `run`
    - Add environment variables:
        + `FLASK_APP=gamestation_app.py`
        + `FLASK_DEBUG=1`
    - Choose your Python interpreter (`python.exe`)

### Following the official flask tutorial
```
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask run
```

As a reference, see:
+ https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/
+ https://github.com/AmI-2017/python-rest