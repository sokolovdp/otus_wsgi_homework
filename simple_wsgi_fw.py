import http.client
import json
import re


class SimpleWSGI:
    def __init__(self):
        self.routes = dict()

    def __call__(self, environ, start_response):

        print('\n\n environ=', dict(environ))

        url = environ['PATH_INFO']
        method = environ['REQUEST_METHOD']
        route_handler, url_args = self.choose_route_handler(url, method)
        status_code, extra_headers, response_content = route_handler(environ, url_args)
        content_type = 'text/plain'
        if not type(response_content) is str:
            response_content = json.dumps(response_content)
            content_type = 'text/json'
        headers = {'Content-Type': content_type, }
        headers.update(extra_headers)

        start_response(f'{status_code} {http.client.responses[status_code]}', list(headers.items()), )
        return [response_content.encode('utf-8')]

    def choose_route_handler(self, url, method):
        route_handler = None
        url_args = None

        if not url.endswith('/'):
            route_handler = SimpleWSGI.no_trailing_slash_route
        else:
            for url_regexp, (current_methods, current_route) in self.routes.items():
                match = re.match(url_regexp, url)
                if match is None:
                    continue
                url_args = match.groupdict()
                if method in current_methods:
                    route_handler = current_route
                else:
                    route_handler = SimpleWSGI.not_allowed_route
                break
            if route_handler is None:
                route_handler = SimpleWSGI.route_not_found

        return route_handler, url_args

    def add_route(self, url: str, methods=None):
        methods = methods or ('GET', )

        def wrapper(route):
            self.routes[url] = methods, route
        return wrapper

    @staticmethod
    def route_not_found(environ, url_args):
        response_content = 'Page not found!'
        return 404, {}, response_content

    @staticmethod
    def not_allowed_route(environ, url_args):
        response_content = 'Method not allowed!'
        return 405, {}, response_content

    @staticmethod
    def no_trailing_slash_route(environ, url_args):
        return 301, {'Location': f"{environ['PATH_INFO']}/"}, 'Moved permanently!'
