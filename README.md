## Simple framework simulation for uWSGI package

**simple_wsgi_fw** - simplest wsgi framework created as otus 2019 web developer course, and based on Ilya Lebedev template. Added: settings for python3 under Ubuntu 19.04, call router handler if method is not allowed, process json data for POST

**test_wsgi_fw** - simulates application which uses the **sokol_router** framework

## To Start uWSGI application test
```
uwsgi --http-socket 127.0.0.1:8000 --ini my_uwsgi.ini
```
## UWSGI ini file
```
[uwsgi]
module = test_uwsgi_fw
plugin = python3
```

## Need to install python3 plugin for uwsgi
```
sudo apt install uwsgi-plugin-python3
```

