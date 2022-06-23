import click


@click.group()
def clients():
    """clients Manages the clients lifecycle
    """
    pass


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


@click.command()
@click.pass_context
def list(ctx):
    """list List all clients

    Args:
        ctx (dict): Dictionary with the rest of the clients
    """
    pass


@click.command()
@click.pass_context
def update(ctx, client_uid):
    """update Updates a client

    Args:
        ctx (dict): Dictionary with the rest of the clients
        client_uid (uid): UID of the user to update
    """


@click.command()
@click.pass_context
def delete(ctx, client_uid):
    """delete Deletes a client

    Args:
        ctx (dict): Dictionary with the rest of the clients
        client_uid (uid): UID of the user to update
    """
    pass


all = clients
