from __future__ import unicode_literals

from models import cons_grammar


rules = [
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
]

start_symbol = 'Sum'

grammar = cons_grammar(rules, start_symbol)

