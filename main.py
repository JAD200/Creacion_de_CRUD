clients = 'Pablo, Ricardo, '


def create_a_client(client_name):
    """create_a_client Adds a client to the list

    Args:
        client_name (str): Name of the client to be added
    """
# ?  Allows the use of variables in the global scope like 'clients'
    global clients

    clients += client_name
    _add_comma()


def _add_comma():
    global clients

    clients += ','


def list_clients():
    global clients

    print(f"\nClients list:\n{clients}")


if __name__ == '__main__':
    list_clients()

    create_a_client('David')

    list_clients()
