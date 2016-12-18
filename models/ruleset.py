from __future__ import unicode_literals

from .side import cons_side
from .rule import cons_rule, is_rule
from .helper import precon


def cons_ruleset(data):
    ruleset = []
    for entry in data:
        ls = entry[0]
        for side in entry[1:]:
            rs = cons_side(side)
            ruleset.append(cons_rule(ls, rs))
    return ruleset


def is_ruleset(obj):
    if not isinstance(obj, list): return False
    for rule in obj:
        if not is_rule(rule):
            return False
    return True


@precon(is_ruleset)
def list_rules(ruleset):
    return ruleset

