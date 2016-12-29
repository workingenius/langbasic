"""
    Unger parser related.

    m cups numbered from 1-m, n marbles from 1-n.
    put sequtive numbered marbles to sequtive numbered cups.
"""

def p(n, m):
    """
    No empty cup.

    in fact, pascal triangle
    """
    assert n >= m
    if m == 1:
        return 1
    if n == m:
        return 1
    else:
        r = 0
        for i in range(1, (n-m+1)+1 ):
            r += p(n-i, m-1)
            # print r
        return r

if __name__ == '__main__':
    print p(200, 5)

def p(n, m):
    """
    empty cups allowed.
    """
    assert n >= m
    if m == 1:
        return 1
    if n == m:
        return 1
    else:
        r = 1
        for i in range(0, (n-m+1)+1 ):
            r += p(n-i, m-1)
            # print r
        return r

if __name__ == '__main__':
    print p(200, 5)
