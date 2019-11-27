import os.path
import argparse
import grammar_converter


class Node:
    def __init__(self, symbol, child1, child2=None):
        self.symbol = symbol
        self.child1 = child1
        self.child2 = child2

    def __repr__(self):
        return self.symbol


class Parser:
    def __init__(self, grammar, sentence):
        self.parse_table = None
        self.prods = {}
        self.grammar = None
        self.input = None
        self.sentence = sentence
        if os.path.isfile(grammar):
            self.grammar_from_file(grammar)
        else:
            self.grammar_from_string(grammar)
        self.__call__(sentence)

    def __call__(self, sentence, parse=False):
        if os.path.isfile(sentence):
            with open(sentence) as inp:
                self.input = inp.readline().split()
                if parse:
                    self.parse()
        else:
            self.input = sentence.split()
            self.sentence = sentence

    def __del__(self):
        print("Closing parser...")

    def grammar_from_file(self, grammar):
        self.grammar = grammar_converter.convert_grammar(grammar_converter.read_grammar(grammar))

    def grammar_from_string(self, grammar):
        self.grammar = grammar_converter.convert_grammar([x.replace("->", "").split() for x in grammar.split("\n")])

    def parse(self):
        length = len(self.input)
        self.parse_table = [[[] for x in range(length - y)] for y in range(length)]

        for i, word in enumerate(self.input):
            for rule in self.grammar:
                if f"'{word}'" == rule[1]:
                    self.parse_table[0][i].append(Node(rule[0], word))
        for words_to_consider in range(2, length + 1):
            for starting_cell in range(0, length - words_to_consider + 1):
                for left_size in range(1, words_to_consider):
                    right_size = words_to_consider - left_size
                    left_cell = []
                    right_cell = []
                    left_cell = self.parse_table[left_size - 1][starting_cell]
                    right_cell = self.parse_table[right_size - 1][starting_cell + left_size]
                    # print(len(left_cell))
                    for rule in self.grammar:
                        left_nodes = [n for n in left_cell if n.symbol == rule[1]]
                        if left_nodes:
                            right_nodes = [n for n in right_cell if n.symbol == rule[2]]
                            self.parse_table[words_to_consider - 1][starting_cell].extend(
                                [Node(rule[0], left, right) for left in left_nodes for right in right_nodes]
                            )

    def print_tree(self, output=True):
        start_symbol = self.grammar[0][0]
        final_nodes = [n for n in self.parse_table[-1][0] if n.symbol == start_symbol]
        if final_nodes:
            if output:
                return True
        else:
            
            print("The given sentence is not contained in the language produced by the given grammar!")
            print(self.sentence)
            return False


def generate_tree(node):
    if node.child2 is None:
        return f"[{node.symbol} '{node.child1}']"
    return f"[{node.symbol} {generate_tree(node.child1)} {generate_tree(node.child2)}]"
