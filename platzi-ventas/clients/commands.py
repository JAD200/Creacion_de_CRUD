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
@click.pass_context
def update(ctx, client_uid):
    """update Updates a client

    Args:
        ctx (dict): Dictionary with the rest of the clients
        client_uid (uid): UID of the user to update
    """


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """delete Deletes a client

    Args:
        ctx (dict): Dictionary with the rest of the clients
        client_uid (uid): UID of the user to update
    """
    pass


all = clients
