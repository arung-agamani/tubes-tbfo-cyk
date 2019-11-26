import re
import os
from rules_lexer import rules
import cyk_parser as parser
import weakref
import datetime as time


file_path = './input_file.txt'

file = open(file_path, 'r')
text = file.read()


class Token(object):
    """
        A simple Token structure.
        Contains the token type, value and position.
    """
    def __init__(self, type, val, pos):
        self.type = type
        self.val = val
        self.pos = pos

    def __str__(self):
        return '%s(%s) at %s' % (self.type, self.val, self.pos)


class LexerError(Exception):
    """ 
        Lexer error exception.
        pos: Position in the input line where the error occurred.
    """
    def __init__(self, pos):
        self.pos = pos


class Lexer(object):
    """ 
        A simple regex-based lexer/tokenizer.
        See below for an example of usage.
    """
    def __init__(self, rules, skip_whitespace=True):
        """ 
            Create a lexer.
            rules:
                A list of rules. Each rule is a `regex, type`
                pair, where `regex` is the regular expression used
                to recognize the token and `type` is the type
                of the token to return when it's recognized.
            skip_whitespace:
                If True, whitespace (\s+) will be skipped and not
                reported by the lexer. Otherwise, you have to
                specify your rules for whitespace, or it will be
                flagged as an error.
        """
        # All the regexes are concatenated into a single one
        # with named groups. Since the group names must be valid
        # Python identifiers, but the token types used by the
        # user are arbitrary strings, we auto-generate the group
        # names and map them to token types.
        #
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
        """ 
            Initialize the lexer with a buffer as input.
        """
        self.buf = buf
        self.pos = 0

    def token(self):
        """ 
            Return the next token (a Token object) found in the
            input buffer. None is returned if the end of the
            buffer was reached.
            In case of a lexing error (the current chunk of the
            buffer matches no rule), a LexerError is raised with
            the position of the error.
        """
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
                # tok = Token(tok_type, m.group(groupname), self.pos)
                tok = tok_type
                self.pos = m.end()
                """ 
                if(tok == 'NEWLINE'):
                    return '\n'
                elif(tok == 'WHITESPACE'):
                    return '' """
                if (tok == 'WHITESPACE') :
                    return ''
                return tok

            # if we're here, no rule matched
            raise LexerError(self.pos)

    def tokens(self):
        """ 
            Returns an iterator to the tokens found in the buffer.
        """
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
    # lx.input('tes = _abc + 12*(R4-623902)  ')
    # print(text)
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
    
    # print(output)
    string_container = output.split('NEWLINE')
    # print("Splitted string : ")
    # print(string_container)
    if_toggle = False
    # parser = cyk_parser

    a_string = " COMMENT "
    start_time = time.datetime.now()
    total_string = len(string_container)
    total_success = 0
    print("Parsing {} line(s) of code...".format(total_string))
    for text in string_container :
        if text == ' ' or text == '' :
            print("",end='')
            total_success += 1
        else :
            if text.find('ELIF') != -1 :
                if if_toggle :
                    text = 'ELIFTOK' + text
                # print(text)
                if process(text) :
                    total_success += 1
            elif text.find('ELSE') != -1 :
                if if_toggle :
                    text = 'ELIFTOK' + text
                # print(text)
                if_toggle = False
                if process(text) :
                    total_success += 1
            elif text.find(' IF ') != -1 :
                # print(text)
                if_toggle = True
                if process(text) :
                    total_success += 1
            else :
                # print(text)
                if process(text) :
                    total_success += 1
    if (total_string == total_success) :
        print("The file is parsed successfully! No errors detected.")
    finish_time = time.datetime.now()
    elapsed_time = finish_time - start_time
    print("Time elapsed : {} microseconds, or {} miliseconds".format(elapsed_time.microseconds, elapsed_time.microseconds/1000))
