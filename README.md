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

## development
```
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask run
```

As a reference, see:
+ https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/
+ https://github.com/AmI-2017/python-rest