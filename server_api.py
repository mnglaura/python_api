from http.server import HTTPServer, BaseHTTPRequestHandler
import database_conn
from graph_ql import execute_mut, execute_query
import api
from orm import get_data_query

data = ""

class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/welcome':
            self.path = '/welcome.html'
        elif self.path =='/get_user.html?get_user=get':
            self.path = '/get_user.html'
        elif self.path =='/post_user.html?create_user=create':
            self.path ='/post_user.html'
        else:
            url = self.path
            data = url.split('?')
            name = data[1].split('=')[1]
            print(name)
            self.send_response(200)
            self.path = api.get_user(name)

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

        #get content length and use to retrieve post data
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        post_data = data.decode('utf-8')
        #post_data is now fname=xxxxx&lname=xxxx, extract two vars from this string
        post_vars = post_data.split('&')
        first_name = post_vars[0].split('=')[1]
        last_name = post_vars[1].split('=')[1]
        query_result = execute_mut(first_name, last_name)
        list_names = get_data_query(query_result)
        api.post_user_function(list_names[0], list_names[1])

        
        

httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()