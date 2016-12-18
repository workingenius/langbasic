from __future__ import unicode_literals

from .symbol import is_symbol, is_terminal
from .side import cons_side, is_side, is_epsilon


# ###
# sentential form


def cons_sentential_form(symbol_list):
    assert is_sentential_form(symbol_list)
    return symbol_list


def is_sentential_form(obj):
    if not isinstance(obj, list): return False
    if not all(map(is_symbol, obj)): return False
    return True


def find_match(sf, side):
    """
    :sf is A valid sentential form

    :return
        List of slices that match.
        If side is epsilon, return [].
    """
    assert is_sentential_form(sf)
    assert is_side(side)
    if is_epsilon(side): return []
    l = len(side)
    retval = []
    for i in range(len(sf)):
        slc = slice(i, i + l)
        c = sf[slc]
        if cons_side(c) == side:
            retval.append( slc )
    return retval


def replace_side(sf, slice, side):
    assert is_sentential_form(sf)
    assert is_side(side)
    sf = sf[:]
    sf[slice] = side
    return sf


# ###
# sentence


def cons_sentence(symbol_list):
    assert is_sentence(symbol_list)
    return symbol_list


def is_sentence(obj):
    if not isinstance(obj, list): return False
    return all(map(is_terminal, obj))

