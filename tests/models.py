from apistar_mongoengine.models import Document
from mongoengine import BooleanField, StringField


class Todo(Document):
    title = StringField(max_length=60)
    text = StringField()
    done = BooleanField(default=False)


class TodoUsingAlias(Document):
    meta = {'db_alias': 'alias'}
    title = StringField(max_length=60)
    text = StringField()
    done = BooleanField(default=False)


class TodoUsingAnotherAlias(Document):
    meta = {'db_alias': 'another_alias'}
    title = StringField(max_length=60)
    text = StringField()
    done = BooleanField(default=False)
