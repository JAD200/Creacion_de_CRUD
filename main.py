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


def create_a_client(client):
    """create_a_client Adds a client to the dictionary

    Args:
        client (str): Name of the client to be added
    """
# ?  Allows the use of variables in the global scope like 'clients'
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('Client is already in the dictionary')


def list_clients():
    print('\nList of clients')
    for index, client in enumerate(clients):
        print(
            f"{index} | {client['name']} | {client['company']} | {client['email']} | {client['position']}")


def _nonexistent_client(client_name):
    """_nonexistent_client Message shown in case the client doesn't exists in the dictionary

    Args:
        client_name (str): Name input by the user
    """
    print(f'Client {client_name} is not in the list')


def update_client(client_name, updated_client_name):
    """update_client Updates the name of an existing client with another

    Args:
        client_name (str): Client to be replaced
        updated_client_name (str): New name of the client replaced
    """
    global clients
    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
        list_clients()
    else:
        _nonexistent_client(client_name)


def delete_client(client_name):
    """delete_client Deletes an existing client

    Args:
        client_name (str): Name of the client to be deleted
    """
    global clients

    if client_name in clients:
        clients.remove(client_name)
        print(f'{client_name} deleted')
    else:
        _nonexistent_client(client_name)


def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('\tWELCOME TO Platzi VENTAS\n' + '*' * 50)
    print('What would you like to do today?')
    print('[C]create client')
    print('[L]list  clients')
    print('[U]update client')
    print('[D]delete client')
    print('[S]search client')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input(f'What is the client {field_name}? ')

    return field


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name? ').title()

        if client_name == 'Exit':
            client_name = None
            break
    if not client_name:
        sys.exit()

    return client_name


if __name__ == '__main__':
    _print_welcome()

    command = input().upper()

    if command == 'C':
        client_name = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }
        create_a_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input(
            'What is the new client name? ').title()
        update_client(client_name, updated_client_name)
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print(f'The client {client_name} is in the list')
        else:
            print(f'The client {client_name} is not in the list')
    else:
        print('Invalid command')
