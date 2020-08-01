from graphene import ObjectType, String, Schema
import graphene
from orm import add_to_model, get_from_model
from api import get_user, post_user_function

class Person(ObjectType):
    first_name = String()
    last_name = String()
    full_name = String()

    def resolve_full_name(parent, info):
        return f"{parent.first_name} {parent.last_name}"

class CreatePerson(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()

    person = graphene.Field(lambda: Person)
    ok = graphene.Boolean()

    def mutate(root, info, first_name,last_name):
        person = Person(first_name=first_name,last_name=last_name)
        add_to_model(first_name, person)
        ok = True
        return CreatePerson(person=person, ok=ok)

class MyMutations(graphene.ObjectType):
    create_person = CreatePerson.Field()

# We must define a query for our schema
class Query(graphene.ObjectType):
    person = graphene.Field(Person, name = graphene.String())

    def resolve_person(parent, info,name):
        return get_from_model(name)


schema = graphene.Schema(query=Query, mutation=MyMutations)


query_mut = 'mutation myMutation($firstName:String, $lastName:String){createPerson(firstName:$firstName, lastName:$lastName){person{firstName,lastName}ok}}'

query_person = '{ person(name: "Peter") {firstName lastName fullName} }'

def execute_mut(first_name, last_name):
    print(first_name)
    result = schema.execute(query_mut, variables = {'firstName':first_name, 'lastName':last_name })
    print(result)
    return result

def execute_query():
    result = schema.execute(query_person)
    print(result)
