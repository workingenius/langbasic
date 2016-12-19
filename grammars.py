from __future__ import unicode_literals

"""
A set of textbook grammars
"""

from models import cons_grammar, epsilon

# TODO:
# consider future situation in which rules should have name or id like "1", "2a", "2b" etc.

__all__ = ['g1', 'g2', ]


# TODO:
# how should we deal with blanks like space?

# Parsing Techs v2 page 23, a PS grammar
g1 = cons_grammar(
    [
        ( ('Name', ), ('tom', ),
                      ('dick', ),
                      ('harry', ) ),
        ( ('Sentence', ), ('Name', ),
                          ('List', 'End', ) ),
        ( ('List', ), ('Name', ),
                      ('Name', ' , ', 'List', ) ),
        ( (' , ', 'Name', 'End'), (' and ', 'Name') ),
    ],
    'Sentence'
)


# Parsing Techs v2 figure 2.6, Monotonic grammar for a[n]b[n]c[n]
g2 = cons_grammar(
    [
        ( ('S', ), ('a', 'b', 'c', ),
                   ('a', 'S', 'Q', ) ),
        ( ('b', 'Q', 'c', ), ('b', 'b', 'c', 'c', ) ),
        ( ('c', 'Q', ), ('Q', 'c', ) ),
    ],
    'S'
)


# Parsing Techs v2 page 30, a CF grammar
g3 = cons_grammar(
    [
        ( ('Name', ), ('tom', ),
                      ('dick', ),
                      ('harry', ), ),
        ( ('Sentence', ), ('Name', ),
                          ('List', ' and ', 'Name', ), ),
        ( ('List', ), ('Name', ' , ', 'List', ),
                      ('Name', ) ),
    ],
    'Sentence',
)


# Parsing Techs v2 page 30, a CF grammar
g4 = cons_grammar(
    [
        ( ('ZeroMotion', ), ('up ', 'ZeroMotion', 'down ', 'ZeroMotion', ),
                            ('down ', 'ZeroMotion', 'up ', 'ZeroMotion', ),
                          # ('left ', 'ZeroMotion', 'right ', 'ZeroMotion', ),
                          # ('right ', 'ZeroMotion', 'left ', 'ZeroMotion', ),
                          epsilon ),
    ],
    'ZeroMotion'
)


# Parsing Techs v2 figure 2.13, regular grammar for a[n]b[n]c[n]
g5 = cons_grammar(
    [
        ( ('Sentence', ) , ('t', ),
                           ('d', ),
                           ('h', ),
                           ('List', ), ),
        ( ('List', ), ('t', 'ListTail', ),
                      ('d', 'ListTail', ),
                      ('h', 'ListTail', ), ),
        ( ('ListTail', ), (', ', 'List', ),
                          (' & ', 't', ),
                          (' & ', 'd', ),
                          (' & ', 'h', ), ),
    ],
    'Sentence'
)


# Parsing Techs v2 figure 2.26
g6 = cons_grammar(
    [
        ( ('Sum', ), ('Digit',),
                     ('Sum', '+', 'Digit') ),
        ( ('Digit', ), ('0', ),
                       ('1', ),
                       ('2', ),
                       ('3', ),
                       ('4', ),
                       ('5', ),
                       ('6', ),
                       ('7', ), )
    ],
    'Sum'
)
