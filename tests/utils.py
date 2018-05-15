import warnings
from mongoengine import connection


def clear_connections_state():
    """
    Mongoengine keep a global state of the connections that must be reset
    before each test. Given it doesn't expose any method to get the list of
    registered connections, we have to do the cleaning by hand
    """
    connection._connection_settings.clear()
    connection._connections.clear()
    connection._dbs.clear()


def force_connect(client):
    """
    Convenience to wait for a newly-constructed client to connect.
    Taken from pymongo test.utils.connected.
    """

    with warnings.catch_warnings():
        # Ignore warning that "ismaster" is always routed to primary even
        # if client's read preference isn't PRIMARY.
        warnings.simplefilter('ignore', UserWarning)
        client.admin.command('ismaster')  # Force connection.

    return client
