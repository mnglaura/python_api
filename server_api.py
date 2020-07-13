from http.server import HTTPServer, BaseHTTPRequestHandler
import database_conn
import api
import cgi, cgitb
from flask import request

class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/welcome':
            self.path = '/welcome.html'
        elif self.path =='/get_user.html?get_user=get':
            self.path = '/get_user.html'
        else:
            self.path ='/post_user.html'

        try: 
            database_conn.create_database()
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        form = cgi.FieldStorage()
        first_name= form.getvalue('fname')
        last_name= form.getvalue('lname')
        print("this is first name" + first_name)
        api.post_user_function(first_name, last_name)



httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()