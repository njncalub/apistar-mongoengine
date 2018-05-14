from apistar_mongoengine.models import Document
from mongoengine import StringField


class PostModel(Document):
    meta = {
        'collection': 'posts',
    }

    message = StringField(required=True)
