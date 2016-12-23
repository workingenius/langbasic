from __future__ import unicode_literals

from .symbol import is_symbol, is_terminal
from .side import cons_side, is_epsilon
from .rule import is_rule, left_side, right_side


# ###
# sentential form


def cons_sentential_form(symbol_list):
    assert is_sentential_form(symbol_list)
    return symbol_list


def is_sentential_form(obj):
    if not isinstance(obj, list): return False
    if not all(map(is_symbol, obj)): return False
    return True


def find_match(sf, rule):
    """
    Find left :side of rule in sentential form :sf

    :return
        List of slices that match.
    """
    assert is_sentential_form(sf)
    assert is_rule(rule)
    side = left_side(rule)
    if is_epsilon(side): return []
    l = len(side)
    retval = []
    for i in range(len(sf)):
        slc = slice(i, i + l)
        c = sf[slc]
        if cons_side(c) == side:
            retval.append( slc )
    return retval


def replace_side(sf, slice, rule):
    """
    Replace sentential form :sf, at position :slice,
    to right side of :rule
    """
    assert is_sentential_form(sf)
    assert is_rule(rule)
    side = right_side(rule)
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

