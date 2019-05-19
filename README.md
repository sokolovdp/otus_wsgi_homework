## Simple framework simulation for uWSGI package

**simple_wsgi_fw** - simplest wsgi framework created as otus 2019 web developer course homework. Code is based on Ilya Lebedev template. Modified: vars and functions names. Added: 
 settings for python3 under Ubuntu 19.04, 
 call router handler if method is not allowed,
 process query params,
 process request body with json data

**test_wsgi_fw** - simulates application which uses the **simple_wsgi_fw** framework

## To start WSGI application test, run:
```
uwsgi --http-socket 127.0.0.1:8000 --ini test_wsgi_fw.ini
```
## UWSGI ini file
```
[uwsgi]
module = test_uwsgi_fw
plugin = python3
```

## To install python3 plugin for UWSGI, run:
```
sudo apt install uwsgi-plugin-python3
```

## Sample of request and response
```
POST: http://127.0.0.1:8000/api/?param1=123&param2=test
BODY: 
{
    "json": "is_working"
}
{
    "remote_ip": "127.0.0.1",
    "query_params": [
        "param1=123",
        "param2=test"
    ],
    "data": {
        "json": "is_working"
    }
}

```