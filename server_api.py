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
        # self.send_response(200)
        # self.send_header('Content-type', 'text/html')
        # self.end_headers()

        # form = cgi.FieldStorage()
        # first_name= form.getvalue('fname')
        # last_name= form.getvalue('lname')
        # print("this is first name" + first_name)

        #get content length and use to retrieve post data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        # print(post_data)
        #post_data is bytes string, convert it to python string using decode
        post_data = post_data.decode('utf-8')
        #post_data is now fname=xxxxx&lname=xxxx, extract two vars from this string
        post_vars = post_data.split('&')
        first_name = post_vars[0].split('=')[1]
        last_name = post_vars[1].split('=')[1]
        api.post_user_function(first_name, last_name)

httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()