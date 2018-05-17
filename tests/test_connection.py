import pytest
from apistar import App, Route, TestClient, http
from apistar_mongoengine.components import MongoClientComponent
from pymongo.errors import ConnectionFailure

from tests.constants import (
    SERVER_SELECTION_TIMEOUT_MS,
    WORKING_ALIAS,
    WORKING_DB,
    WORKING_HOST,
    WORKING_PORT,
)
from tests.models import Todo


def test_simple_connect_using_params(sconn_params):
    client = sconn_params.resolve()
    response = client.admin.command("ismaster")

    assert response
    assert isinstance(response, dict)


def test_simple_connect_using_host_string(sconn_host):
    client = sconn_host.resolve()
    response = client.admin.command("ismaster")

    assert response
    assert isinstance(response, dict)


def test_simple_connect_using_host_string_mongomock(sconn_mockhost):
    from mongomock.mongo_client import MongoClient

    client = sconn_mockhost.resolve()
    assert isinstance(client, MongoClient)


def test_simple_connect_using_invalid_port(sconn_invalid_port):
    client = sconn_invalid_port.resolve()

    with pytest.raises(ConnectionFailure):
        client.admin.command("ismaster")


def test_disconnect_client(sconn_params):
    client1 = sconn_params.resolve()
    sconn_params.disconnect()
    client2 = sconn_params.resolve()

    assert client1 is not client2


def test_data_persists(sconn_params):
    Todo.drop_collection()

    todo = Todo()
    todo.text = "Sample"
    todo.title = "Testing"
    todo.done = True

    new_todo = todo.save()
    fetched_todo = Todo.objects().first()

    assert new_todo.pk == fetched_todo.pk
    assert new_todo.title == fetched_todo.title
    assert new_todo.text == fetched_todo.text
    assert new_todo.done == fetched_todo.done


def test_basic_app(sconn_params):
    HARDCODED_TODO_ID = "1234567890abcdef12345678"

    Todo.drop_collection()

    def post_todo() -> http.JSONResponse:
        todo = Todo()
        todo.id = HARDCODED_TODO_ID
        todo.text = "Sample"
        todo.title = "Testing"
        todo.done = True
        new_todo = todo.save()

        data = {
            "id": str(new_todo.id),
            "text": new_todo.text,
            "title": new_todo.title,
            "done": new_todo.done,
        }

        return http.JSONResponse(data, status_code=201)

    def get_todo() -> dict:
        fetched_todo = Todo.objects().first()

        data = {
            "id": str(fetched_todo.id),
            "text": fetched_todo.text,
            "title": fetched_todo.title,
            "done": fetched_todo.done,
        }

        return data

    routes = [
        Route(url="/todo/", method="POST", handler=post_todo),
        Route(url="/todo/", method="GET", handler=get_todo),
    ]

    options = {
        "host": WORKING_HOST,
        "port": WORKING_PORT,
        "name": WORKING_DB,
        "alias": WORKING_ALIAS,
        "serverSelectionTimeoutMS": SERVER_SELECTION_TIMEOUT_MS,
    }

    components = [MongoClientComponent(**options)]

    app = App(routes=routes, components=components)
    client = TestClient(app)

    new_todo = client.post("/todo/")

    assert new_todo.status_code == 201
    assert (
        new_todo.json()
        == {
            "id": HARDCODED_TODO_ID,
            "text": "Sample",
            "title": "Testing",
            "done": True,
        }
    )

    fetched_todo = client.get("/todo/")

    assert fetched_todo.status_code == 200
    assert fetched_todo.json() == new_todo.json()
