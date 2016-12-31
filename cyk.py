# -*- coding:utf8 -*-
from __future__ import unicode_literals
from pprint import pprint
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
    """
    :epsilon_symbols is a set containing symbols that will possibly generate epsilon
    """
    def _match(recog_table, symbols, start_index, substring_length):
        assert isinstance(symbols, (tuple, list))

        if is_epsilon(symbols):
            return 
        assert len(symbols) > 0

        sym = symbols[0]
        substring = sentence[start_index: start_index + substring_length]
        if len(symbols) == 1:
            if is_non_terminal(sym):
                if sym in epsilon_symbols:
                    if len(substring) == 0:
                        yield [(sym, 0)]
                    else:
                        return
                elif recog_table.contains( (substring_length, start_index), symbols[0]):
                    yield [(sym, substring_length)]
                else:
                    return
            elif is_terminal(sym):
                if sym == substring[0] and len(substring) == 1:
                    yield [(sym, 1)]
                else:
                    return
        else:
            if is_non_terminal(sym):
                if sym in epsilon_symbols:
                    for sd in _match(recog_table, symbols[1:],
                            start_index, substring_length):
                        # sd for sub_derivation
                        yield [(sym, 0)] + sd
                for sssl in range(1, substring_length):
                    # sssl for sub-sub-string length
                    if recog_table.contains( (sssl, start_index), sym):
                        for sd in _match(recog_table, symbols[1:], start_index + sssl,
                                substring_length - sssl):
                            yield [(sym, sssl)] + sd
                    else:
                        return
            elif is_terminal(sym):
                if sym == substring[0]:
                    for sd in _match(recog_table, symbols[1:], start_index + 1,
                            substring_length - 1):
                        yield [(sym, 1)] + sd
                else:
                    return

    def match(*args, **kwargs):
        """
        Make match result hashable
        """
        for d in _match(*args, **kwargs):
            yield tuple(d)

    for start_idx in range(len(sentence) - sub_length + 1):
        has_new = False
        for rule in rules:
            start_symbol, symbols = left_side(rule)[0], right_side(rule)
            # print symbols, start_idx, sub_length
            for derivation in match(recog_table, symbols, start_idx, sub_length):
                # print derivation
                is_new = recog_table.insert( (sub_length, start_idx), start_symbol, derivation )
                has_new = has_new or is_new
        while has_new:
            has_new = False
            for rule in rules:
                start_symbol, symbols = left_side(rule)[0], right_side(rule)
                for derivation in match(recog_table, symbols, start_idx, sub_length):
                    is_new = recog_table.insert( (sub_length, start_idx), start_symbol, derivation )
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
            ( ('D', ), ('D', 'd', ),   # has ref to epsilon but not chain rule  -> false
                ('B', 'd', ) ),
            ( ('E', ), ('C', 'C', 'B', ) ),   # all symbol can be epsilon  -> true
        ],
        'A'
    )
    print symbols_generating_epsilon(list_rules(get_ruleset(g)))


    sen = cons_sentential_form(['@'], trace=False)
    pprint(cyk_recognise(g, sen))

    sen = cons_sentential_form('d d $ d'.split(), trace=False)
    pprint(cyk_recognise(g, sen))


#! 函数参数太多,且中间总是变化的时候,容易出错;这说明每个procedure的概念,用途不清晰.原料和产出不清晰.
#! 用function generate, 使用方法应当用for. 这点经常出错
#! range的结尾是不生成的,这点总是出错
#! recog table的数据结构代表的意义还是不清晰
