from __future__ import unicode_literals

from .helper import precon
from .ruleset import is_ruleset, list_rules, cons_ruleset
from .rule import left_side
from .symbol import is_non_terminal


def cons_grammar(rule_list, start_symbol):
    ruleset = cons_ruleset(rule_list)
    assert is_grammar( (ruleset, start_symbol) )
    return (ruleset, start_symbol)


def is_grammar(obj):
    if not isinstance(obj, tuple): return False
    if len(obj) != 2: return False

    ruleset, start_symbol = obj
    if not is_ruleset(ruleset): return False
    if not is_non_terminal(start_symbol): return False
    rules = list_rules(ruleset)
    for rule in rules:
        if (start_symbol, ) == left_side(rule):
            return True
    return False
    

@precon(is_grammar)
def get_ruleset(grammar):
    return grammar[0]


@precon(is_grammar)
def get_start_symbol(grammar):
    return grammar[1]

