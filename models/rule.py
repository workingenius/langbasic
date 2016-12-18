from __future__ import unicode_literals

from .helper import precon
from .side import is_side, is_epsilon


def is_rule(obj):
    if not isinstance(obj, tuple): return False
    if len(obj) != 2: return False
    return True if is_side(obj[0]) and is_side(obj[1]) and not is_epsilon(obj[0]) else False


@precon(is_rule)
def left_side(rule):
    return rule[0]


@precon(is_rule)
def right_side(rule):
    return rule[1]

