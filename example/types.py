from apistar import types, validators


class PostType(types.Type):
    message = validators.String()
