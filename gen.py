def generate_sentences(rules, start_rule):
    """
    :rules
        rules = [
           ((Left-side), (Right-side)),
           ((Left-side), (Right-side)),
        ]
    """
    q = [[start_rule]]

    while True:
        # sentential form
        sf = q.pop()

        if all(map(is_terminal, sf)):
            output(sf)
            continue

        for rule in rules:
            left_side, right_side = rule

            # new sentiential forms
            nsfs = list(
                    replace(sf, left_side, right_side)
                    )
            q = nsfs + q
            # print q


def find_match(parent, child):
    assert isinstance(parent, list)
    assert isinstance(child, (list, tuple))
    l = len(child)
    assert l > 0

    for i in range(len(parent)):
        c = parent[i: i+l]
        if tuple(c) == tuple(child):
            yield i


def replace(sf, left_side, right_side):
    """
    """
    result = []
    for idx in list(find_match(sf, left_side)):
        _sf = sf[:]
        _sf[idx : idx + len(left_side)] = list(right_side)
        result.append(_sf)

    # result = reversed(result)
    return result


def is_terminal(token):
    assert isinstance(token, basestring)
    if token.lower() == token: return True
    else: return False


def output(sf):
    assert isinstance(sf, list)
    print ''.join(sf)
