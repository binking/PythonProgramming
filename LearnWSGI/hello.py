def application(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html")]) # start_response is a function
    body_html = "<H1>Hello, %s !</H1>" % (env['PATH_INFO'][1:] or 'Web')
    return [body_html.encode('utf-8')]
