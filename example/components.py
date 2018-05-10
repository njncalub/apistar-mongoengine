from apistar_mongoengine.components import MongoClientComponent


components = [
    MongoClientComponent(
        alias='default',
        host='mongodb://localhost:27017/blog'
    ),
]
