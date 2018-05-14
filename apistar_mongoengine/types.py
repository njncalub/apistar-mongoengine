from typing import (
    List,
    Mapping,
    NewType,
    Sequence,
    Tuple,
    Union,
)

from apistar import types as apistar_types


PageLimit = NewType('PageLimit', int)
PageOffset = NewType('PageOffset', int)
PageCount = NewType('PageCount', int)
PageResults = NewType('PageResults', List)

StrPairs = Sequence[Tuple[str, str]]
StrMapping = Mapping[str, str]
StrObjMapping = Mapping[str, object]


class Paginated(StrObjMapping):
    """
    Modified code from apistar.http.QueryParams.
    """

    def __init__(self,
                 value: Union[StrMapping, StrPairs]=None) -> None:
        if value is None:
            value = []
        if hasattr(value, 'items'):
            items = list(value.items())
        else:
            items = list(value)
        self._dict = {k: v for k, v in reversed(items)}
        self._list = items

    def get_list(self, key: str) -> List[str]:
        return [
            item_value for item_key, item_value in self._list
            if item_key == key
        ]

    def keys(self):
        return [key for key, value in self._list]

    def values(self):
        return [value for key, value in self._list]

    def items(self):
        return list(self._list)

    def get(self, key, default=None):
        if key in self._dict:
            return self._dict[key]
        else:
            return default

    def __getitem__(self, key):
        return self._dict[key]

    def __contains__(self, key):
        return key in self._dict

    def __iter__(self):
        return iter(self._list)

    def __len__(self):
        return len(self._list)

    def __eq__(self, other):
        if not isinstance(other, Paginated):
            other = Paginated(other)
        return sorted(self._list) == sorted(other._list)

    def __repr__(self):
        return 'Paginated({})'.format(repr(self._list))


class Type(apistar_types.Type):
    pass
