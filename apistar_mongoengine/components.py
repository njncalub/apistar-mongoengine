from apistar import Component
from mongoengine import connection as me_connection
from mongoengine.python_support import IS_PYMONGO_3
from pymongo import MongoClient, ReadPreference


if IS_PYMONGO_3:
    READ_PREFERENCE = ReadPreference.PRIMARY
else:
    from pymongo import MongoReplicaSetClient
    READ_PREFERENCE = False


class MongoClientComponent(Component):
    def __init__(self, **kwargs) -> None:
        """
        Configure a new database backend.
        
        View self.register_connection() for valid parameters.
        """
        
        options = {
            'alias': me_connection.DEFAULT_CONNECTION_NAME,
        }
        options.update(kwargs)
        
        self.register_connection(**options)
    
    def resolve(self) -> MongoClient:
        return self.get_connection()
    
    def register_connection(self, **kwargs) -> MongoClient:
        """
        Register a new connection. Taken from mongoengine-0.15.0.
        
        :param alias: the name that will be used to refer to this connection
            throughout MongoEngine
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
        
        me_connection.register_connection(**kwargs)
        
        alias = kwargs['alias']
        
        return self.get_connection(alias=alias)
    
    def get_connection(self, **kwargs) -> MongoClient:
        """
        Return a MongoClient connection. Taken from mongoengine-0.15.0.
        
        :param alias: the name that will be used to refer to this connection
            throughout MongoEngine
        :param reconnect: Connect to the database if not already connected
        """
        
        me_connection.get_connection(**kwargs)


class PaginationComponent(Component):
    pass
