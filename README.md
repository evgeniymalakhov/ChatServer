# ChatServer

[![Python|Django](https://www.fullstackpython.com/img/logos/django.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This is the template server for feature project with video/audio chat on Python.

# New Features!
  - Socket chat is written on Django Channels
  - SignIn/SignUp are implemented via allauth lib

### Tech

Dillinger uses a number of open source projects to work properly:

* [Redis] - Redix DB using for chat server
* [Django] - Django web framework of 3.0.3 version 

All you need to follow the instruction to run development server.

### Installation

Install virtual environment with python of 3.8 version and activate this environment
```sh
$ python3.8 -m venv venv
$ source /venv/bin/activate
```
Requires [Python](https://www.python.org/downloads/release/python-380/) v3.8 to start project.

Install all requirements from file to your virtual environment

```sh
$ pip install -r requirements.txt
```

For production chat server it's better to use Redis. You can easily install redis server via docker, just type the command
```sh
docker run -p 6379:6379 -d redis:2.8
```

And in the main settings you just need to config your redis layer
```sh
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
```
if you would like to test chat without Redis, you just can type current layer in settings.py and that's all 
```sh
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}
```

To start local server just type command below.

```sh
python manage.py runserver 0.0.0.0:8000
```

License
----
**Free Software!**
