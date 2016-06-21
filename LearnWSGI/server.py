from wsgiref.simple_server import make_server
from hello import application

httpd = make_server("", 8080, application) # ip is empty and port is 8000 and call application processing function
print("...Serving HTTP on port 8080...")
httpd.serve_forever()
