import click
#   Tabulate
#   for more info: https://bit.ly/3brDT3K
from tabulate import tabulate
#   Services and models
from clients.services import ClientService
from clients.models import Client


@click.group()
def clients():
    """clients Manages the clients lifecycle
    """
    pass


@clients.command()
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help='The client name')
@click.option('-c', '--company',
              type=str,
              prompt=True,
              help='The client company')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='The client email')
@click.option('-p', '--position',
              type=str,
              prompt=True,
              help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """create Creates a new client

    Args:
        ctx (dict): Dictionary with the rest of the clients
        name (str): Name of the client to create
        company (str): Company of the client to create
        email (str): Email of the client to create
        position (str): Current work position of the client to create
    """
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """list List all clients

    Args:
        ctx (dict): Dictionary with the rest of the clients
    """
    client_service = ClientService(ctx.obj['clients_table'])

    clients_list = client_service.list_clients()

    headers = [field.upper() for field in Client.schema()]
    table = []

    for client in clients_list:
        table.append([
            client['name'],
            client['company'],
            client['email'],
            client['position'],
            client['uid']])

    click.echo(tabulate(table, headers))


@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def update(ctx, client_uid):
    """update Updates a client

    Args:
        ctx (dict): Dictionary with the rest of the clients
        client_uid (uid): UID of the user to update
    """
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()

    client = [client for client in client_list if client['uid'] == client_uid]

    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)

        click.echo('Client updated')
    else:
        click.echo('Client uid does not exists\nClient not updated')


def _update_client_flow(client):
    click.echo('\n\tLeave empty if you don\'t want to modify the value')

    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)

    return client


@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def delete(ctx, client_uid):
    """delete Deletes a client

    Args:
        ctx (dict): Dictionary with the rest of the clients
        client_uid (uid): UID of the user to update
    """
    pass


all = clients
