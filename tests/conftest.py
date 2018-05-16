import pytest
from apistar_mongoengine.components import MongoClientComponent

from tests.constants import (
    NON_WORKING_PORT,
    SERVER_SELECTION_TIMEOUT_MS,
    WORKING_ALIAS,
    WORKING_DB,
    WORKING_HOST,
    WORKING_PORT,
)
from tests.utils import clear_connections_state


@pytest.fixture
def sconn_params():
    """
    Simple connection component using different parametrs.
    """
    clear_connections_state()

    options = {
        'host': WORKING_HOST,
        'port': WORKING_PORT,
        'name': WORKING_DB,
        'alias': WORKING_ALIAS,
        'serverSelectionTimeoutMS': SERVER_SELECTION_TIMEOUT_MS,
    }
    return MongoClientComponent(**options)


@pytest.fixture
def sconn_host():
    """
    Simple connection component using a host string.
    """
    clear_connections_state()

    options = {
        'host': f'mongodb://{WORKING_HOST}:{WORKING_PORT}/{WORKING_DB}',
        'serverSelectionTimeoutMS': SERVER_SELECTION_TIMEOUT_MS,
    }
    return MongoClientComponent(**options)


@pytest.fixture
def sconn_mockhost():
    """
    Simple connection component using a mock host string.
    """
    clear_connections_state()

    options = {
        'host': f'mongomock://{WORKING_HOST}:{WORKING_PORT}/{WORKING_DB}',
        'serverSelectionTimeoutMS': SERVER_SELECTION_TIMEOUT_MS,
    }
    return MongoClientComponent(**options)


@pytest.fixture
def sconn_invalid_port():
    """
    Simple connection component using an invalid port number.
    """
    clear_connections_state()

    options = {
        'host': WORKING_HOST,
        'port': NON_WORKING_PORT,
        'name': WORKING_DB,
        'serverSelectionTimeoutMS': SERVER_SELECTION_TIMEOUT_MS,
    }
    return MongoClientComponent(**options)
