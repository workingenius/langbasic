# -*- coding:utf8 -*-
"""
unger parser first version
"""
#TODO: grammar with loop
#TODO: duplicate question will cause infinte recursion
#TODO: visualize production tree
#TODO: with epsilon
#TODO: sementic

from __future__ import unicode_literals
from pprint import pprint

from grammars import g3, g4
from models.sentence import SententialFrom
from models.grammar import get_ruleset, get_start_symbol
from models.ruleset import list_rules
from models.rule import left_side, right_side
from models.side import cons_side
from models.symbol import is_terminal, is_non_terminal


# Q:
#   1. how to represent a production tree, with what kind of data structure
#   2. how to adhere each sentential form with a unfinished parse tree
#   3. if hard-code parse tree logic in generate_sentences, they are coupled tightly -> automata
#   4. generate_sentences algrithm is too slow, too memery-eating, and lack further consideration
#       so it is not practical, and may break down in many situations.


def _divide(sentence, part_num):
    """
    :return all partitions of the sentence, as a list
    """
    assert len(sentence) >= part_num, \
        'len(sentence): {}, part_num: {}'.format(len(sentence), part_num)
    if part_num == 1:
        yield [sentence]
    elif len(sentence) == part_num:
        yield [[s] for s in sentence]
    else:
        #! range和slice有时总出错
        for i in range(1, len(sentence) - part_num + 1 + 1):
            for sub_div in _divide(sentence[i:], part_num-1):
                r = [sentence[:i]]
                r.extend(sub_div)
                yield r


# if __name__ == '__main__':
#     for d in _divide(range(200), 5):
#         print d


def unger_parse(grammar, sentence):
    # unger parser
    # parse一个sentence,给出一个grammar和一个sentence,找到production tree
    # 从start symbol开始找
    # 最基本的思路是,遍历所有的可能性,一一匹配.如果找到生成树,则parse成功.若所有可能性都不能成功,则此语法不能生成此sentence
    # 所有的可能性?
    # 所有以此symbol为左侧的rule,若parse成功,则必至少有一个右侧最终能展开成此sentence
    # 如何知道某个右侧能够成为sentence?
    # 对sentence进行partition操作,若右侧有N个symbol,则把sentence分为N各相邻的部分,每个部分对应一个symbol;
    # 若parse成功,必有至少一个partition方法对应某个rule的右侧
    # 如果rule的右侧是terminal,那么sentence当中的该部分与之相等时,才对应.否则不对应
    # 如果某个rule的右侧是non-terminal,那么sentence当中的该part能被该non-terminal展开,才对应.否则不对应.
    # 

    def _sub_rule_list(symbol):
        """
        :return a sub-rule_list from :grammar, each of which has :symbol as its left side.
        """
        rl = list_rules(get_ruleset(grammar))
        #! 从这里看出来,对象还是没抽象好
        return [r for r in rl if left_side(r) == cons_side([symbol])]

    def all_situations(start_symbol, sentence):
        rules      = _sub_rule_list(start_symbol)
        for rule in rules:
            rs = right_side(rule)
            if len(sentence) < len(rs):
                continue
            partitions = _divide(sentence, len(rs))
            for partition in partitions:
                yield (rs, partition)

    def cons_pt(start_symbol, side, parts):
        #import pdb; pdb.set_trace()
        symbols = side
        pt = [start_symbol]
        for symbol, part in zip(symbols, parts):
            if is_terminal(symbol):
                if symbol != part[0] or len(part) != 1:
                    return None
                else:
                    pt.append(symbol)
            elif is_non_terminal(symbol):
                sub_pt = parse(symbol, part)
                if sub_pt:
                    pt.append(sub_pt)
                else:
                    return None
        return pt

    def parse(start_symbol, sentence):
        assert isinstance(sentence, list)
        for situation in all_situations(start_symbol, sentence):
            # construct production tree with child production tree
            side, parts = situation
            pt = cons_pt(start_symbol, side, parts)
            if pt:
                return pt
            
    return parse(get_start_symbol(grammar), sentence.symbol_list)


if __name__ == '__main__':
    pprint( unger_parse(g3, SententialFrom(['harry'])) )
    pprint( unger_parse(g3, SententialFrom(['tom', ' , ' , 'dick', ' and ', 'harry'])) )
    pprint( unger_parse(g3, SententialFrom(['tom', ' , ' , 'dick', ' , ', 'tom', ' and ', 'harry'])) )
    pprint( unger_parse(g3, SententialFrom(['tom', ' , ' , 'dick', ' , ', 'tom', ' , ', 'harry'])) )  # None

    # TODO
    # pprint( unger_parse(g4, SententialFrom(['up', 'down', 'down', 'down', 'up', 'up'])) )
