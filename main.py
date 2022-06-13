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


def _print_welcome():
    print('WELCOME TO Platzi VENTAS\n', '*' * 50)
    print('What would you like to do today?')
    print('[C]create client')
    print('[D]delete client')


if __name__ == '__main__':
    _print_welcome()

    command = input()

    if command == 'C' or command == 'c':
        client_name = input('Como se llama el usuario a añadir?')
        create_a_client(client_name)
        list_clients()
    elif command == 'D' or command == 'd':
        clients_name = input('Como se llama el usuario a borrar?')
    else:
        print('Invalid command')
