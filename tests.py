from graph_ql import schema
from user_data import dict_user
from api import get_user, post_user_function

query_mut = 'mutation myFirstMutation ($first_name, $last_name){'\
    'createPerson(firstName:$first_name, lastName:$last_name) {'\
        'person {'\
            'firstName,'\
            'lastName,'\
            'fullName'\
        '}'\
        'ok'\
    '}'\
'}'

def execute_mut():
    result = schema.execute(query_mut, variables = {'first_name':dict_user['firstName'], 'last_name':dict_user['lastName'] })
    print(result)
    post_user_function(result.data['createPerson']['person']['firstName'], result.data['createPerson']['person']['lastName'])


query_person = '{ person(name: "Peter") {firstName lastName fullName} }'

def execute_query():
    result = schema.execute(query_person)
    print(result)
