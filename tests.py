from graph_ql import schema
from api import get_user, post_user_function

query_mut = 'mutation myMutation($firstName:String, $lastName:String){createPerson(firstName:$firstName, lastName:$lastName){person{firstName,lastName}ok}}'

query_person = '{ person(name: "Peter") {firstName lastName fullName} }'

def execute_mut(first_name, last_name):
    print(first_name)
    result = schema.execute(query_mut, variables = {'firstName':first_name, 'lastName':last_name })
    print(result)
    post_user_function(result.data['createPerson']['person']['firstName'], result.data['createPerson']['person']['lastName'])
    print('success')

def execute_query():
    result = schema.execute(query_person)
    print(result)
