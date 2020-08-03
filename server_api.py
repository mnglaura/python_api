from http.server import HTTPServer, BaseHTTPRequestHandler
import database_conn
from graph_ql import execute_mut, execute_query
import api
from orm import get_data_query
from urls import get_request_mapper

data = ""

class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        database_conn.create_database()
        print('self path:'+self.path)
        self.path = get_request_mapper(self.path)
        try: 
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