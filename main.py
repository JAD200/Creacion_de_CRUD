clients = 'Pablo, Ricardo, '


def create_a_client(client_name):
    """create_a_client Adds a client to the list

    Args:
        client_name (str): Name of the client to be added
    """
# ?  Allows the use of variables in the global scope like 'clients'
    global clients
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client is already in the clients list')


def _add_comma():
    global clients

    clients += ','


def list_clients():
    global clients

    print(f"\nClients list:\n{clients}")


def _nonexistent_client(client_name):
    """_nonexistent_client Message shown in case the client doesn't exists in the list

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
        clients = clients.replace(client_name, updated_client_name)
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
        clients = clients.replace(client_name + ',', '')
        list_clients()
    else:
        _nonexistent_client(client_name)


def _print_welcome():
    print('WELCOME TO Platzi VENTAS\n' + '*' * 50)
    print('What would you like to do today?')
    print('[C]create client')
    print('[U]update client')
    print('[D]delete client')


def _get_client_name():
    return input('What is the client name? ').capitalize()


if __name__ == '__main__':
    _print_welcome()

    command = input().upper()

    if command == 'C':
        client_name = _get_client_name()
        create_a_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input(
            'What is the new client name? ').capitalize()
        update_client(client_name, updated_client_name)
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
    else:
        print('Invalid command')
