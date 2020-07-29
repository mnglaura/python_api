from server_api import data

dict_user = {}

def get_names():
    post_data = data.decode('utf-8')
    post_vars = post_data.split('&')
    dict_user['firstName'] = post_vars[0].split('=')[1]
    dict_user['lastName'] = post_vars[1].split('=')[1]
   


