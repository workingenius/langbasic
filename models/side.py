from __future__ import unicode_literals

from .symbol import is_symbol


epsilon = tuple()


def cons_side(symbols):
    symbols = tuple(symbols)
    assert is_side(symbols)
    return symbols


def is_side(obj):
    if not isinstance(obj, tuple): return False
    return True if all(map(is_symbol, obj)) else False


def is_epsilon(obj):
    return obj == epsilon

