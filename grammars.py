from __future__ import unicode_literals

"""
A set of textbook grammars
"""

from models import grammar

# TODO:
# type grammar with literals are really annoying

# TODO:
# consider future situation in which rules should have name or id like "1", "2a", "2b" etc.

__all__ = ['g1', 'g2', ]


# TODO:
# how should we deal with blanks like space?

# Parsing Techs v2 page 23, a PS grammar
g1 = grammar(
    [
        ( ('Name', ), ('tom', ) ),
        ( ('Name', ), ('dick', ) ),
        ( ('Name', ), ('harry', ) ),
        ( ('Sentence', ), ('Name', ) ),
        ( ('Sentence', ), ('List', 'End', ) ),
        ( ('List', ), ('Name', ) ),
        ( ('List', ), ('Name', ' , ', 'List', ) ),
        ( (' , ', 'Name', 'End'), (' and ', 'Name') ),
    ],
    'Sentence'
)


# Parsing Techs v2 figure 2.6, Monotonic grammar for a[n]b[n]c[n]
g2 = grammar(
    [
        ( ('S', ), ('a', 'b', 'c', ) ),
        ( ('S', ), ('a', 'S', 'Q', ) ),
        ( ('b', 'Q', 'c', ), ('b', 'b', 'c', 'c', ) ),
        ( ('c', 'Q', ), ('Q', 'c', ) ),
    ],
    'S'
)

