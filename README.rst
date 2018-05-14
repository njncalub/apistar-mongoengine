apistar-mongoengine
===================

|development status| |pypi version|

.. |development status| image:: https://img.shields.io/badge/development%20status-planning-lightgrey.svg
   :target: https://github.com/njncalub/apistar-mongoengine/issues

.. |pypi version| image:: https://img.shields.io/badge/version-0.0.5-blue.svg
   :target: https://pypi.org/project/apistar-mongoengine/0.0.5

Shameless bootleg copy of `flask-mongoengine <https://github.com/MongoEngine/flask-mongoengine/>`_ for `API Star <https://github.com/encode/apistar>`_, modified for personal taste. Contributions are most welcome!

Installation
------------

::

    $ pip install apistar-mongoengine

Getting Started
---------------

For your classes, use ``Document`` and ``DocumentType`` from ``apistar_mongoengine.models``.

::

    from apistar_mongoengine.models import Document, DocumentType
    from mongoengine import StringField


    class ItemModel(Document):
        meta = {
            'collection': 'items',
        }

        title = StringField(required=True)


    class ItemType(DocumentType):
        meta = {
            'model': ItemModel,
        }


Add ``MongoClientComponent`` to your app's components to initialize the mongodb connection.

::

    import typing

    from apistar import App, Route
    from apistar_mongoengine.components import MongoClientComponent

    from yourapp.models import ItemModel, ItemType


    def list_items() -> typing.List[ItemType]:
        return [
            ItemType(item)
            for item in ItemModel.objects.all()
        ]

    routes = [
        Route(url='/items/', method='GET', handler=list_items),
    ]

    components = [
        MongoClientComponent(host='mongodb://localhost:27017/sample'),
    ]

    app = App(routes=routes, components=components)


    if __name__ == '__main__':
        app.serve(host='127.0.0.1', port=5000, debug=True)

Check the `example <https://github.com/njncalub/apistar-mongoengine/tree/master/example>`_ for more details.

Contributing
------------

**Imposter syndrome disclaimer**: We want your help. No, really.

There may be a little voice inside your head that is telling you that you're not ready to be an open source contributor; that your skills aren't nearly good enough to contribute. What could you possibly offer a project like this one?

We assure you - the little voice in your head is wrong. If you can write code at all, you can contribute code to open source. Contributing to open source projects is a fantastic way to advance one's coding skills. Writing perfect code isn't the measure of a good developer (that would disqualify all of us!); it's trying to create something, making mistakes, and learning from those mistakes. That's how we all improve, and we are happy to help others learn.

Being an open source contributor doesn't just mean writing code, either. You can help out by writing documentation, tests, or even giving feedback about the project (and yes - that includes giving feedback about the contribution process). Some of these contributions may be the most valuable to the project as a whole, because you're coming to the project with fresh eyes, so you can see the errors and assumptions that seasoned contributors have glossed over.

License
-------

MIT licensed. Please see the bundled `LICENSE file <https://github.com/njncalub/apistar-mongoengine/blob/master/LICENSE>`_ for more details.
