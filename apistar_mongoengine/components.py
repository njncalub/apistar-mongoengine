from apistar import Component
from mongoengine import connection as me_conn
from pymongo import MongoClient


class MongoClientComponent(Component):
    def __init__(self, **kwargs) -> None:
        """
        Configure a new database backend.

        :param alias: the name that will be used to refer to this connection
            throughout MongoEngine
        :param db: alias to `name`
        :param name: the name of the specific database to use
        :param host: the host name of the :program:`mongod` instance to
            connect to
        :param port: the port that the :program:`mongod` instance is running on
        :param read_preference: The read preference for the collection
           ** Added pymongo 2.1
        :param username: username to authenticate with
        :param password: password to authenticate with
        :param authentication_source: database to authenticate against
        :param authentication_mechanism: database authentication mechanisms.
            By default, use SCRAM-SHA-1 with MongoDB 3.0 and later,
            MONGODB-CR (MongoDB Challenge Response protocol) for older servers.
        :param is_mock: explicitly use mongomock for this connection
            (can also be done by using `mongomock://` as db host prefix)
        :param kwargs: ad-hoc parameters to be passed into the pymongo driver,
            for example maxpoolsize, tz_aware, etc. See the documentation
            for pymongo's `MongoClient` for a full list.
        """

        options = {
            'alias': me_conn.DEFAULT_CONNECTION_NAME,
            'db': None,
            'name': None,
        }
        options.update(kwargs)
        self.settings = options.copy()

        alias = options.pop('alias')
        # since me_conn.connect() uses `db` instead of `name`,
        # we have to remove it here manually.
        db = options.pop('db')
        name = options.pop('name')

        if not db and name:
            db = name

        self.connection = me_conn.connect(db=db, alias=alias, **options)

    def get_connection(self) -> MongoClient:
        """
        Return the current connection.
        """

        if self.connection:
            return self.connection

        alias = self.settings.get('alias')
        self.connection = me_conn.get_connection(alias=alias)

        return self.connection

    def disconnect(self) -> None:
        alias = self.settings['alias']
        me_conn.disconnect(alias=alias)

    def resolve(self) -> MongoClient:
        return self.get_connection()


class PaginationComponent(Component):
    pass
