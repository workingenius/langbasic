"""
Implementation predicates of chomsky hierachy
"""

from models import is_terminal


# ################
# epsilon-free types


def is_grammar(grammar):
    try:
        assert isinstance(grammar, tuple)
        rules, start_symbol = grammar
        assert isinstance(rules, list)
        assert isinstance(start_symbol, basestring)
        for r in rules:
            assert isinstance(r, tuple)
            assert len(r) == 2
            assert not is_terminal(r[0])
            assert len(r[1]) > 0  # epsilon-free
    except Exception:
        return False
    finally:
        return True


def is_type0(grammar):
    """
    PS(Phrase Structure) grammar, formal grammar without any limit
    """
    assert is_grammar(grammar)
    return True


def is_type1(grammar):
    """
    CS(Context Sensitive) grammar

    As CS grammar is equavalent to Monotonic grammar, the later is implemented
    """
    assert is_grammar(grammar)
    rules, _ = grammar
    for rule in rules:
        left_side, right_side = rule
        if len(left_side) > len(right_side):
            return False
    return True


def is_type2(grammar):
    """
    CF(Context Free) grammar

    All rules whose left-side only contains one non-terminal and without any terminal
    """
    assert is_grammar(grammar)
    rules , _ = grammar
    for rule in rules:
        left_side, right_side = rule
        if len(left_side) > 1:
            return False
    return True


def is_type3(grammar):
    """
    Regular grammar

    Based on type2, and the right-side must contains only one non-terminal that locate at the end
    """
    if not is_type2(grammar):
        return False
    rules , _ = grammar
    for rule in rules:
        left_side, right_side = rule
        for symbol in right_side[:-1]:
            if not is_terminal(symbol):
                return False
        if is_terminal(right_side[-1]):
            return False
    return True


def is_type4(grammar):
    """
    FC(Finite Choice) grammar

    all right-sides contains only terminals
    """
    assert is_grammar(grammar)
    rules , _ = grammar
    for rule in rules:
        for symbol in rule[1]:
            if not is_terminal(symbol):
                return False
    return True



if __name__ == '__main__':

    import grammars as gs

    assert is_grammar(gs.g1)
    assert is_type0(gs.g1)
    assert not is_type1(gs.g1)

    assert is_type0(gs.g2)
    assert is_type1(gs.g2)
    assert not is_type2(gs.g2)

