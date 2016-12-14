def is_terminal(symbol):
    assert isinstance(symbol, basestring) and len(symbol) > 0
    c = symbol[0]
    if c.lower() != c: return False
    else: return True

