from __future__ import unicode_literals

from models import cons_grammar


rules = [
    ( ('Sum', ), ('Digit',) ),
    ( ('Sum', ), ('Sum', '+', 'Digit') ),
    ( ('Digit', ), ('0', ) ),
    ( ('Digit', ), ('1', ) ),
    ( ('Digit', ), ('2', ) ),
    ( ('Digit', ), ('3', ) ),
    ( ('Digit', ), ('4', ) ),
    ( ('Digit', ), ('5', ) ),
    ( ('Digit', ), ('6', ) ),
    ( ('Digit', ), ('7', ) ),
]

start_symbol = 'Sum'

grammar = cons_grammar(rules, start_symbol)

