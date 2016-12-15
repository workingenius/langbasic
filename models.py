from __future__ import unicode_literals

"""
    overview:

        Symbol  : string
            Terminal     : Symbol all lowercase
            NonTerminal : Symbol started with uppercase letter
            StartSymbol : Symbol
        Side    : tuple
        Rule    : (Side, Side)
        Rules   : [Rule, ...]
        Grammar : (Rules, StartSymbol)

        SententialForm  : [Symbol, ...]
        Sentence        : [NonTerminal, ...]
"""


# ################
# symbol


def is_symbol(obj):
    if not isinstance(obj, unicode):
        return False
    if len(obj) <= 0:
        return False
    return True


def is_terminal(symbol):
    if not is_symbol(symbol): return False
    c = symbol[0]
    if c.lower() != c: return False
    else: return True


def is_non_terminal(symbol):
    if not is_symbol(symbol): return False
    return not is_terminal(symbol)


# ################
# side


def is_side(obj):
    if not isinstance(obj, tuple): return False
    return True if all(map(is_symbol, obj)) else False


def is_epsilon(obj):
    if not is_side(obj): return False
    return True if len(obj) == 0 else False


# ################
# rule


def is_rule(obj):
    if not isinstance(obj, tuple): return False
    if len(obj) != 2: return False
    return True if is_side(obj[0]) and is_side(obj[1]) and not is_epsilon(obj[0]) else False


def left(rule):
    return rule[0]


def right(rule):
    return rule[1]


# ################
# grammar


def grammar(rule_list, start_symbol):
    """
    grammar constructor
    """
    g = (rule_list, start_symbol)
    must_grammar(g)
    return g


G = grammar


def is_grammar(grammar):
    try:
        assert_grammar(grammar)
    except AssertionError:
        return False
    finally:
        return True


def must_grammar(grammar):
    rule_list, start_symbol = grammar
    assert isinstance(rule_list, list), \
        'rule_list should be a list, not {}'.format(type(rule_list))
    assert len(rule_list) > 0, 'empty rule_list'
    assert all(map(is_rule, rule_list)), 'non-rule in rule_list'
    assert is_symbol(start_symbol), \
        'invalid start_symbol: {}'.format(start_symbol)
    assert (start_symbol, ) in map(left, rule_list), \
        'start_symbol {} is not in any rule'.format(start_symbol)

