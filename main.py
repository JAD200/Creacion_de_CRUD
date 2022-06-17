import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer'
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data engineer'
    }
]


def create_a_client(client_to_add):
    """create_a_client Adds a client to the dictionary

    Args:
        client_to_add (dict): Information of the client to be created
    """
# ?  Allows the use of variables in the global scope like 'clients'
    global clients
    if client not in clients:
        clients.append(client)
        list_clients()
    else:
        print('Client is already in the dictionary')


def list_clients():
    print('\nList of clients')
    for index, client in enumerate(clients):
        print(
            f"{index} | {client['name']} | {client['company']} | {client['email']} | {client['position']}")


def _nonexistent_client(client_id):
    """_nonexistent_client Message shown in case the client doesn't exists in the dictionary

    Args:
        client_id (int): Name input by the user
    """
    print(f'Client {client_id} is not in the list')


def update_client(client_id):
    """update_client Updates the name of an existing client with another

    Args:
        client_id (int): Client to be replaced
    """
    global clients
    if len(clients) - 1 >= client_id and client_id >= 0:
        updated_client = _get_client_from_user()
        clients[client_id] = updated_client
        list_clients()
    else:
        _nonexistent_client(client_id)


def delete_client(client_id):
    """delete_client Deletes an existing client

    Args:
        client_id (int): UID of the client to be deleted
    """
    global clients

    for index, client in enumerate(clients):
        if index == client_id:
            del clients[index]
            print(f"""Client {client_id} deleted""")
            break
    else:
        _nonexistent_client(client_id)


def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _get_client_field(field_name):
    field = None

    while not field:
        field = input(f'What is the client {field_name}? ')

    return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name').title(),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position').capitalize(),
    }

    return client


def _print_welcome():
    print('\tWELCOME TO Platzi VENTAS\n' + '*' * 50)
    print('What would you like to do today?')
    print('[C]create client')
    print('[L]list  clients')
    print('[U]update client')
    print('[D]delete client')
    print('[S]search client')


if __name__ == '__main__':
    _print_welcome()

    command = input().upper()

    if command == 'C':
        client_to_add = {
            'name': _get_client_field('name').title(),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position').capitalize()
        }
        create_a_client(client_to_add)
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        update_client(client_id)
    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
    elif command == 'S':
        client_name = _get_client_field('name').title()
        found = search_client(client_name)
        if found:
            print(f'The client {client_name} is in the list')
        else:
            print(f'Sadly, the client {client_name} is not in the list')
    else:
        print('Invalid command')
