from typing import Any, Iterable

__version__ = "0.0.1"
__all__ = [
    '__version__', 'find', 'find_one',
]

_none = object()


def _find(source, key, value, path=()):
    if value is not _none and source == value:
        yield path, value

    if isinstance(source, dict):
        if key is not _none and key in source:
            yield path + (key,), source[key]

        for k, v in source.items():
            yield from _find(v, key, value, path=path + (k,))

    elif isinstance(source, (bytes, str)):
        return

    elif isinstance(source, Iterable):
        for i, item in enumerate(source):
            yield from _find(item, key, value, path + (i,))


def find(source: Any, *, key: Any = _none, value: Any = _none):
    return _find(source, key=key, value=value)


def find_one(source: Any, *, key: Any = _none, value: Any = _none):
    for res in find(source, key=key, value=value):
        return res
