from __future__ import unicode_literals

from .rule import is_rule
from .helper import precon


def cons_ruleset(rule_list):
    for rule in rule_list:
        assert is_rule(rule), '{} is not a valid rule'.format(rule)
    return rule_list


def is_ruleset(obj):
    if not isinstance(obj, list): return False
    for rule in obj:
        if not is_rule(rule):
            return False
    return True


@precon(is_ruleset)
def list_rules(ruleset):
    return ruleset

