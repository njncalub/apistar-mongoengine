from apistar_mongoengine.components import MongoClientComponent

from settings import DATABASE_URL


components = [MongoClientComponent(host=DATABASE_URL)]
