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

    def clone(self):
        return SententialFrom(self.symbol_list[:])

    def find_match(self, rule):
        """
        Find left :side of rule in sentential form :self

        :return
            List of slices that match.
        """
        assert is_rule(rule)

        sl = self.symbol_list
        side = left_side(rule)

        if is_epsilon(side): return []
        l = len(side)
        retval = []
        for i in range(len(sl)):
            slc = slice(i, i + l)
            c = sl[slc]
            if cons_side(c) == side:
                retval.append( slc )
        return retval

    def replace_side(self, slice, rule):
        """
        Replace sentential form :self, at position :slice,
        to right side of :rule
        """
        assert is_rule(rule)
        sf = self.clone()
        sf.symbol_list[slice] = right_side(rule)
        return sf

    def __unicode__(self):
        return ''.join(self.symbol_list)


class SententialFormWithPT(SententialFrom):
    """
    Sentential form with production tree
    """
    def __init__(self, symbol_list, pt=None):
        super(self.__class__, self).__init__(symbol_list)
        self.pt = pt or []

    def clone(self):
        return SententialFormWithPT(self.symbol_list[:], self.pt[:])

    def replace_side(self, slice, rule):
        sf = super(self.__class__, self).replace_side(slice, rule)
        sf.pt.append( (slice.start, rule) )
        return sf

    def __unicode__(self):
        return ''.join(self.symbol_list) + '\n' + unicode(self.pt)


def cons_sentential_form(symbol_list, trace=True):
    if trace:
        return SententialFormWithPT(symbol_list)
    else:
        return SententialFrom(symbol_list)


def is_sentential_form(obj):
    return isinstance(obj, SententialFrom)


def find_match(sf, rule):
    """
    Find left :side of rule in sentential form :sf

    :return
        List of slices that match.
    """
    assert is_sentential_form(sf)
    return sf.find_match(rule)


def replace_side(sf, slice, rule):
    """
    Replace sentential form :sf, at position :slice,
    to right side of :rule
    """
    assert is_sentential_form(sf)
    return sf.replace_side(slice, rule)


# ###
# sentence


def is_sentence(obj):
    return isinstance(obj, SententialFrom) and obj.is_sentence()
