Set up tests
============

1. Run ``mongod``. For the tests, we assume that Mongo DB is running on ``localhost:27017``

.. code:: bash

    $ mongod --port 27017

1. Open a separate terminal and install the requirements using ``pipenv``

.. code:: bash

    $ pipenv install --dev -e .

2. Run the app

.. code:: bash

    $ pipenv run pytest
