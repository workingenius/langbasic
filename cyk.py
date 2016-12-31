from __future__ import unicode_literals
from models import *


class RecognationTable(dict):
    def insert(self, substring_index, start_symbol, derivation):
        v = (start_symbol, derivation)
        key = substring_index
        if key in self:
            if v in self[key]:
                return False
            else:
                self[key].add(v)
                return True
        else:
            self[key] = {v}
            return True

    def contains(self, substring_index, start_symbol):
        key = substring_index
        if not (key in self):
            return False
        else:
            for ssym, _ in self[key]:
                if ssym == start_symbol:
                    return True
            return False


def symbols_generating_epsilon(rule_list):
    """
    Must be cf grammar rule_list
    """
    e_syms = set()
    o_syms = set([left_side(rule)[0] for rule in rule_list])
    for rule in rule_list:
        sym, rs = left_side(rule)[0], right_side(rule)
        if is_epsilon(rs):
            e_syms.add(sym)
    while len(e_syms & o_syms):
        o_syms = o_syms - e_syms
        for sym in o_syms:
            for rule in [r for r in rule_list if left_side(r)[0] == sym]:
                if all([(_sym in e_syms) for _sym in right_side(rule)]):
                    e_syms.add(sym)
    return e_syms
    

def _cyk_recognise_step(rules, sentence, recog_table, sub_length, epsilon_symbols):
    def match(recog_table, symbols, start_index, substring_length, epsilon_symbols):
        """
        :epsilon_symbols is a set containing symbols that will possibly generate epsilon
        """
        assert isinstance(symbols, (tuple, list))
        if is_epsilon(symbols):
            return
        elif len(symbols) == 1:
            # TODO
            if recog_table.contains( (substring_length, start_index), symbols[0]):
                yield [(symbols[0], substring_length)]
            else:
                return
        else:
            sym = symbols[0]
            if sym in epsilon_symbols:
                # sub_derivation
                for sd in match(recog_table, symbols[1:],
                        start_index, substring_length, epsilon_symbols):
                    yield [(symbols[0], 0)] + sd
            for sssl in range(1, substring_length):
                # sssl for sub-sub-string length
                for sd in match(recog_table, symbols[1:], start_index + sssl,
                        substring_length - sssl, epsilon_symbols):
                    yield [(symbols[0], sssl)] + sd


    for start_idx in range(len(sentence) - sub_length):
        has_new = False
        for rule in rules:
            start_symbol, symbols = left_side(rule)[0], right_side(rule)
            for derivation in match(recog_table, symbols, start_idx, sub_length):
                is_new = recog_table.insert( (sub_length, start_idx), derivation )
                has_new = has_new or is_new
        while has_new:
            has_new = False
            for rule in rules:
                start_symbol, symbols = left_side(rule)[0], right_side(rule)
                for derivation in match(recog_table, symbols, start_idx, sub_length):
                    is_new = recog_table.insert( (sub_length, start_idx), derivation )
                    has_new = has_new or is_new

    return recog_table


def cyk_recognise(grammar, sentence):
    sentence = sentence.symbol_list
    rules = list_rules(get_ruleset(grammar))
    rec_t = RecognationTable()
    e_syms = symbols_generating_epsilon(rules)
    for l in xrange(1, len(sentence) + 1):
        rec_t = _cyk_recognise_step(rules, sentence, rec_t, l, e_syms)
    return rec_t


if __name__ == '__main__':
    g = cons_grammar(
        [ 
            ( ('A', ), ('C', '@', 'C', ), ('B', '#', 'B', ), ('D', '$', 'D' ), ('E', '^', 'E', ) ),
            ( ('B', ), epsilon ),   # epsilon directly  -> true
            ( ('C', ), ('B', ) ),   # epsilon in chain rule  -> true
            ( ('D', ), ('D', 'd', ) ),   # has ref to epsilon but not chain rule  -> false
            ( ('E', ), ('C', 'C', 'B', ) ),   # all symbol can be epsilon  -> true
        ],
        'A'
    )
    print symbols_generating_epsilon(list_rules(get_ruleset(g)))


    sen = cons_sentential_form(['@'], trace=False)
    print cyk_recognise(g, sen)
