rules = [
    (r'from', 'FROM'),
    (r'import', 'IMPORT'),
    (r'as\s', 'AS'),
    (r'class', 'CLASS'),
    (r'def', 'DEF'),
    (r'return', 'RETURN'),
    (r'pass', 'PASS'),
    (r'raise', 'RAISE'),
    (r'continue', 'CONTINUE'),
    (r'break', 'BREAK'),
    (r'if', 'IF'),
    (r'elif', 'ELIF'),
    (r'else', 'ELSE'),
    (r'for', 'FOR'),
    (r'in', 'IN'),
    (r'range', 'RANGE'),
    (r'while', 'WHILE'),
    (r'None', 'NONE'),
    (r'True', 'TRUE'),
    (r'False', 'FALSE'),
    (r'not', 'NOT'),
    (r'and', 'AND'),
    (r'or', 'OR'),
    (r'is', 'IS'),
    (r'with', 'WITH'),
    (r'print', 'PRINT'),
    (r'len', 'LEN'),
    (r'str', 'STR'),
    (r'int', 'INT'),
    (r'float', 'FLOAT'),
    (r'bool', 'BOOL'),
    (r'abs', 'ABS'),
    (r'round', 'ROUND'),
    (r'pow', 'POW'),
    (r'input', 'INPUT'),

    (r'\"\"\"[\w|\s]*\"\"\"', 'COMMENT'),
    (r'\#.*', 'COMMENT'),
    ('\".+\"', 'STRING'),
    ('\'.+\'', 'STRING'),
    (r'\.', 'WITH_METHOD'),
    (r':', 'COLON'),
    (r'\n', 'NEWLINE'),
    (r' ', 'WHITESPACE'),
    (r'\d+',             'NUMBER'),
    (r'[a-zA-Z_]+',    'IDENTIFIER'),
    # (r'[a-zA-Z_]\w+',    'IDENTIFIER'),
    (r'\+',              'PLUS'),
    (r'\-',              'MINUS'),
    (r'\*\*',              'POWER'),
    (r'\*',              'MULTIPLY'),
    (r'\/',              'DIVIDE'),
    (r'\(',              'LP'),
    (r'\)',              'RP'),
    (r'==', 'DOUBLEEQUAL'),
    (r'=',               'EQUALS'),
    (r',', 'COMA'),
    (r'>=', 'GREATER_OR_EQUAL_THAN'),
    (r'>', 'GREATER_THAN'),
    (r'<=', 'LESS_OR_EQUAL_THAN'),
    (r'<', 'LESS_THAN'),
]