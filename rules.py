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

start_rules = 'Sum'
