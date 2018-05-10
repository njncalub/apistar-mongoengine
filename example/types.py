from apistar import validators
from apistar_mongoengine.types import Type


class PostType(Type):
    message = validators.String()
