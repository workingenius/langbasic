from __future__ import unicode_literals

from .symbol import is_symbol, is_terminal
from .side import cons_side, is_epsilon
from .rule import is_rule, left_side, right_side


# ###
# sentential form


class SententialFrom(object):
    def __init__(self, symbol_list):
        assert self.verify(symbol_list)
        self.symbol_list = symbol_list

    def verify(self, symbol_list):
        obj = symbol_list
        if not isinstance(obj, list): return False
        if not all(map(is_symbol, obj)): return False
        return True

    def is_sentence(self):
        return len(self.symbol_list) and all(map(is_terminal, self.symbol_list))

    def __unicode__(self):
        return ''.join(self.symbol_list)


cons_sentential_form = SententialFrom


def is_sentential_form(obj):
    return isinstance(obj, SententialFrom)


def find_match(sf, rule):
    """
    Find left :side of rule in sentential form :sf

    :return
        List of slices that match.
    """
    assert is_sentential_form(sf)
    assert is_rule(rule)

    sf = sf.symbol_list
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
    sf = sf.symbol_list
    side = right_side(rule)
    sf = sf[:]
    sf[slice] = side
    return cons_sentential_form(sf)


# ###
# sentence


def is_sentence(obj):
    return isinstance(obj, SententialFrom) and obj.is_sentence()
