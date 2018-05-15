apistar-mongoengine
===================

|development status| |pypi version| |build status| |coverage|

.. |development status| image:: https://img.shields.io/badge/development%20status-planning-lightgrey.svg
   :target: https://github.com/njncalub/apistar-mongoengine/issues

.. |pypi version| image:: https://img.shields.io/badge/version-0.0.5-blue.svg
   :target: https://pypi.org/project/apistar-mongoengine

.. |build status| image:: https://travis-ci.org/njncalub/apistar-mongoengine.svg?branch=master
    :target: https://travis-ci.org/njncalub/apistar-mongoengine

.. |coverage| image:: https://coveralls.io/repos/github/njncalub/apistar-mongoengine/badge.svg?branch=master
   :target: https://coveralls.io/github/njncalub/apistar-mongoengine?branch=master


Shameless bootleg copy of `flask-mongoengine <https://github.com/MongoEngine/flask-mongoengine/>`_ for `API Star <https://github.com/encode/apistar>`_, modified for personal taste. Contributions are most welcome!

Installation
------------

.. code:: bash

    $ pip install apistar-mongoengine

Getting Started
---------------

For your classes, use ``Document`` from ``apistar_mongoengine.models``.

.. code:: python

    from apistar_mongoengine.models import Document
    from mongoengine import StringField

    class TodoItem(Document):
        title = StringField(required=True)

Add ``MongoClientComponent`` to your app's components to initialize the mongodb connection.

.. code:: python

    from apistar import App, Route
    from apistar_mongoengine.components import MongoClientComponent
    from yourapp.models import TodoItem

    def list_items():
        return [
            item.title
            for item in TodoItem.objects.all()
        ]

    routes = [
        Route(url='/items/', method='GET', handler=list_items),
    ]
    components = [
        MongoClientComponent(host='mongodb://localhost:27017/todoapp'),
    ]

    app = App(routes=routes, components=components)

    if __name__ == '__main__':
        app.serve(host='127.0.0.1', port=5000, debug=True)

Check the `example <https://github.com/njncalub/apistar-mongoengine/tree/master/example>`_ for more details.

Running tests and getting the test coverage
-------------------------------------------

1. Install the required dependencies

.. code:: bash

    $ cd <project directory>
    $ pipenv install

2. Run ``pytest`` with ``coverage`` flags

.. code:: bash

    $ pipenv run pytest --cov-report html --cov apistar_mongoengine/ --verbose

3. Open ``./htmlcov/index.html`` in your browser.

Contributing
------------

**Imposter syndrome disclaimer**: We want your help. No, really.

There may be a little voice inside your head that is telling you that you're not ready to be an open source contributor; that your skills aren't nearly good enough to contribute. What could you possibly offer a project like this one?

We assure you - the little voice in your head is wrong. If you can write code at all, you can contribute code to open source. Contributing to open source projects is a fantastic way to advance one's coding skills. Writing perfect code isn't the measure of a good developer (that would disqualify all of us!); it's trying to create something, making mistakes, and learning from those mistakes. That's how we all improve, and we are happy to help others learn.

Being an open source contributor doesn't just mean writing code, either. You can help out by writing documentation, tests, or even giving feedback about the project (and yes - that includes giving feedback about the contribution process). Some of these contributions may be the most valuable to the project as a whole, because you're coming to the project with fresh eyes, so you can see the errors and assumptions that seasoned contributors have glossed over.

License
-------

MIT licensed. Please see the bundled `LICENSE file <https://github.com/njncalub/apistar-mongoengine/blob/master/LICENSE>`_ for more details.
