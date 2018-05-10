from apistar_mongoengine.components import MongoClientComponent


components = [
    MongoClientComponent(host='mongodb://localhost:27017/blog'),
]
