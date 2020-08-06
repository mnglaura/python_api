import api

def get_params(path):
	"""check if get parameters in the path. return a list
	   in format of [path, params]
	"""
	if '?' in path:
		return path.split('?')
	else: 
		return [path,None]		

def fetch_template(path):
	"""This will return the templates path
	   from templates folder.  
	"""
	return '/templates'+path+'.html'

def fetch_user_name(path,params):
	"""read params for name and fetch name from api"""
	name = params.split('=')[1]
	success_path = api.get_user(name)
	success_path_template = fetch_template(success_path)
	return success_path_template

def get_request_mapper(path):
	"""This will match the path to the given action from
	   path_list_action dictionary. It will then call the 
	   action as a function and return the result. Params
	   will be sent if not empty.
	"""
	path, params = get_params(path)

	if path in path_list_action:
		action = path_list_action[path]
		if params:
			result = action(path,params)
		else:
			result = action(path)
		return result

#This list maps urls with their main functions. 
#To add new url, you must add it to this list.
path_list_action = {
	'/welcome': fetch_template,
	'/get_user': fetch_template,
	'/post_user': fetch_template,
	'/user-details': fetch_user_name,
}