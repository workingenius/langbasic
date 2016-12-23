from __future__ import unicode_literals

from functools import wraps
from time import sleep

from models import *


def output(sf):
    assert isinstance(sf, list)
    print ''.join(sf)


# ################
# generator


def generate_sentences(grammar):
    """
    generate all legal sentences with the given grammar
    """

    assert is_grammar(grammar)
    ruleset, start_symbol = get_ruleset(grammar), get_start_symbol(grammar)
    q = [cons_sentential_form([start_symbol])]

    while True:
        sf = q.pop()

        if is_sentence(sf):
            output(sf)
            continue

        for rule in list_rules(ruleset):
            ls, rs = left_side(rule), right_side(rule)

            slices = find_match(sf, rule)
            for slc in slices:
                nsf = replace_side(sf, slc, rule)
                q = [nsf] + q
                break

        # print q
        # sleep(0.1)


if __name__ == '__main__':
    from grammars import g1

    generate_sentences(g1)

