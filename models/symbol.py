from __future__ import unicode_literals

from .helper import non_strict, precon


"""
symbol is any object that implements valid __eq__, except empty string
"""


def is_symbol(obj):
    if obj == '': return False
    return True


@precon(is_symbol, 'a terminal should be a symbol')
def is_terminal(obj):
    if isinstance(obj, basestring) and obj[0].lower() == obj[0]:
        return True
    else: return False


@precon(is_symbol, 'a non-terminal should be a symbol')
def is_non_terminal(obj):
    if isinstance(obj, basestring) and obj[0].lower() != obj[0]:
        return True
    else: return False

