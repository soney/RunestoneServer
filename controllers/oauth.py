
def index():
    full_url = '%s://%s%s' % (request.env.wsgi_url_scheme, request.env.http_host,
                   request.env.web2py_original_uri)
    return {'url': full_url}