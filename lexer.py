import re
import os
from rules_lexer import rules
import cyk_parser as parser
import datetime as time

input_file = input("Input file to check : ")

file_path = './' + input_file
file = open(file_path, 'r')
text = file.read()

class Token(object):
    def __init__(self, type, val, pos):
        self.type = type
        self.val = val
        self.pos = pos

    def __str__(self):
        return '%s(%s) at %s' % (self.type, self.val, self.pos)


class LexerError(Exception):
    def __init__(self, pos):
        self.pos = pos


class Lexer(object):
    def __init__(self, rules, skip_whitespace=True):
        idx = 1
        regex_parts = []
        self.group_type = {}

        for regex, type in rules:
            groupname = 'GROUP%s' % idx
            regex_parts.append('(?P<%s>%s)' % (groupname, regex))
            self.group_type[groupname] = type
            idx += 1

        self.regex = re.compile('|'.join(regex_parts))
        self.skip_whitespace = skip_whitespace
        self.re_ws_skip = re.compile('\S')

    def input(self, buf):
        self.buf = buf
        self.pos = 0

    def token(self):
        if self.pos >= len(self.buf):
            return None
        else:
            if self.skip_whitespace:
                m = self.re_ws_skip.search(self.buf, self.pos)

                if m:
                    self.pos = m.start()
                else:
                    return None

            m = self.regex.match(self.buf, self.pos)
            if m:
                groupname = m.lastgroup
                tok_type = self.group_type[groupname]
                tok = tok_type
                self.pos = m.end()
                if (tok == 'WHITESPACE') :
                    return ''
                return tok
            raise LexerError(self.pos)

    def tokens(self):
        while 1:
            tok = self.token()
            if tok is None: 
                break
            yield tok

CYK = parser.Parser('grammar.txt', " COMMENT ")

def process(sentence) :
    CYK.__call__(sentence)
    CYK.parse()
    return CYK.print_tree()

if __name__ == '__main__':

    lx = Lexer(rules, skip_whitespace=False)
    lx.input(text)
    output = ''

    try:
        for tok in lx.tokens():
            if tok == '' :
                output = output
            else :
                output += tok + ' '
    except LexerError as err:
        print('LexerError at position %s' % err.pos)
    
    string_container = output.split('NEWLINE')
    if_toggle = 0
    start_time = time.datetime.now()
    total_string = len(string_container)
    total_success = 0
    total_error = 0
    line_counter = 0
    print("Parsing {} line(s) of code...".format(total_string))
    for text in string_container :
        line_counter += 1
        if text == ' ' or text == '' :
            print("",end='')
            total_success += 1
        else :
            if text.find(' IF') != -1 :
                if_toggle += 1
                if process(text) :
                    total_success += 1
                else :
                    print("Error at line {}.".format(line_counter))
                    total_error += 1
            elif text.find('ELIF') != -1 :
                if if_toggle > 0 :
                    text = 'ELIFTOK' + text
                if process(text) :
                    total_success += 1
                else :
                    print("Error at line {}.".format(line_counter))
                    total_error += 1
            elif text.find('ELSE') != -1 :
                if if_toggle > 0 :
                    text = 'ELIFTOK' + text
                if_toggle -= 1
                if process(text) :
                    total_success += 1
                else :
                    print("Error at line {}.".format(line_counter))
                    total_error += 1
            else :
                if process(text) :
                    total_success += 1
                else :
                    print("Error at line {}.".format(line_counter))
                    total_error += 1
    if (total_string == total_success) :
        print("The file is parsed successfully! No errors detected.")
    else :
        print("{} Error(s) detected on the file.".format(total_error))
    finish_time = time.datetime.now()
    elapsed_time = finish_time - start_time
    print("Time elapsed : {}.{} seconds".format(elapsed_time.seconds, elapsed_time.microseconds//1000))
