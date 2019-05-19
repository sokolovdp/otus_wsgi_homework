from simple_wsgi_fw import SimpleWSGI


application = SimpleWSGI()  # application is the name UWSGI is looking for in the module


@application.add_route(r'^/$', methods=('GET', 'POST'))
def index_page_handler(environ, url_args):
    return 200, {}, 'Index'


@application.add_route(r'^/api/$', methods=('POST', ))
def info_page_handler(environ, url_args):
    return 200, {}, {
        'remote_ip': environ['REMOTE_ADDR'],
        'url_agrs': url_args,
    }


@application.add_route(r'^/user/(?P<user_id>\d+)/$')
def info_page_handler(environ, url_args):
    return 200, {}, {'user_id': url_args['user_id']}
