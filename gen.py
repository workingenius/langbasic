"""
    Symbol  : string
        Terminal     : Symbol all lowercase
        NonTerminal : Symbol started with uppercase letter
        StartSymbol : Symbol
    Side    : tuple
    Rule    : (Side, Side)
    Rules   : [Rule, ...]
    Grammar : (Rules, StartSymbol)

    SententialForm : [Symbol, ...]
    Sentence        : [NonTerminal, ...]
"""

from functools import wraps

from models import is_terminal


# ################
# utils


def to_list(func):
    """
    :func
        a callable that return a iter
    """
    @wraps(func)
    def nf(*args, **kwargs):
        return list(func(*args, **kwargs))
    return nf


def output(sf):
    assert isinstance(sf, list)
    print ''.join(sf)


def replace(lst, slice, sub_list):
    assert isinstance(lst, list)
    l = lst[:]
    l[slice] = list(sub_list)
    return l


# ################
# generator


def generate_sentences(grammar):
    """
    generate all legal sentences with the given grammar
    """
    rules, start_symbol = grammar
    q = [[start_symbol]]

    while True:
        # sentential form
        sf = q.pop()

        if all(map(is_terminal, sf)):
            output(sf)
            continue

        for rule in rules:
            left_side, right_side = rule

            slices = find_match(sf, left_side)
            for slc in slices:
                nsf = replace(sf, slc, right_side)
                q = [nsf] + q


@to_list
def find_match(parent, child):
    assert isinstance(parent, list)
    assert isinstance(child, (list, tuple))
    l = len(child)
    assert l > 0

    for i in range(len(parent)):
        slc = slice(i, i+l)
        c = parent[slc]
        if tuple(c) == tuple(child):
            yield slc

