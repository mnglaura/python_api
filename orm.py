
dict_data = {}


def add_to_model(person,name):
    dict_data[name] = person

def get_from_model(name):
    return dict_data[name]


def get_data_query(result):
    names_list = []
    first_name = result.data['createPerson']['person']['firstName']
    last_name = result.data['createPerson']['person']['lastName']
    names_list.append(first_name)
    names_list.append(last_name)
    print(names_list)
    return names_list