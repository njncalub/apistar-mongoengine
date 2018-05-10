from apistar import types, validators


class PostType(types.Type):
    id = validators.String()
    message = validators.String()
