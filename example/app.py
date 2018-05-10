#!/usr/bin/env python
# coding=utf-8

import os
import sys

path = os.path.realpath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.insert(0, path)

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
