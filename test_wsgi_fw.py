import json
from simple_wsgi_fw import SimpleWSGI


application = SimpleWSGI()  # application is the name UWSGI is looking for in the module


@application.add_route(r'^/$', methods=('GET', 'POST'))
def index_page_handler(environ, url_args, query_params, request_body):
    return 200, {}, 'Index'


@application.add_route(r'^/api/$', methods=('POST', ))
def info_page_handler(environ, url_args, query_params, request_body):
    if request_body:
        data = json.loads(request_body)
    else:
        data = {}
    return 200, {}, {
        'remote_ip': environ['REMOTE_ADDR'],
        'query_params': query_params,
        'data': data
    }


@application.add_route(r'^/user/(?P<user_id>\d+)/$')
def info_page_handler(environ, url_args, query_params, request_body):
    return 200, {}, {'user_id': url_args['user_id']}
