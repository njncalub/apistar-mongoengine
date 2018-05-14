from apistar import App

from routes import routes
from components import components
from event_hooks import event_hooks


app = App(routes=routes,
          components=components,
          event_hooks=event_hooks)


if __name__ == '__main__':
    default = {
        'host': '127.0.0.1',
        'port': 5000,
        'debug': True,
    }

    app.serve(**default)
