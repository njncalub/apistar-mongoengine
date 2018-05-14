import pytest

from apistar_mongoengine.models import Document
from apistar_mongoengine.components import MongoClientComponent
from mongoengine import BooleanField, StringField


@pytest.fixture
def sconn_comp_params():
    """
    Simple connection component using different parametrs.
    """
    options = {
        'host': 'localhost',
        'port': 27017,
        'name': 'apistar_mongoengine_test_db',
    }
    return MongoClientComponent(**options)


@pytest.fixture
def sconn_comp_host():
    """
    Simple connection component using a host string.
    """
    options = {
        'host': 'mongodb://localhost:27017/apistar_mongoengine_test_db',
    }
    return MongoClientComponent(**options)


@pytest.fixture
def sconn_comp_mockhost():
    """
    Simple connection component using a mock host string.
    """
    options = {
        'host': 'mongomock://localhost:27017/apistar_mongoengine_test_db',
    }
    return MongoClientComponent(**options)


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


def test_simple_connect_using_params(sconn_comp_params):
    client = sconn_comp_params.resolve()

    assert client['host'] == 'localhost'
    assert client['port'] == 27017
    assert client['name'] == 'apistar_mongoengine_test_db'
    assert client['alias'] == 'default'


def test_simple_connect_using_host_string(sconn_comp_host):
    client = sconn_comp_host.resolve()

    assert client['host'] == 'localhost'
    assert client['port'] == 27017
    assert client['name'] == 'apistar_mongoengine_test_db'
    assert client['alias'] == 'default'


def test_simple_connect_using_host_string_mongomock(sconn_comp_mockhost):
    client = sconn_comp_mockhost.resolve()

    assert client['host'] == 'localhost'
    assert client['port'] == 27017
    assert client['name'] == 'apistar_mongoengine_test_db'
    assert client['alias'] == 'default'
    assert client['is_mock'] == True


def test_data_persists(sconn_comp_params):
    Todo.drop_collection()

    todo = Todo()
    todo.text = 'Sample'
    todo.title = 'Testing'
    todo.done = True

    new_todo = todo.save()
    fetched_todo = Todo.objects().first()

    assert new_todo.pk == fetched_todo.pk
    assert new_todo.title == fetched_todo.title
    assert new_todo.text == fetched_todo.text
    assert new_todo.done == fetched_todo.done
