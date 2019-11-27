rules = [
    (r'\"\"\"[\w|\s|\d|\(|\)|\{|\}|\[|\]\=|\.|\:|\'|\"|\,]*\"\"\"', 'COMMENT'),
    (r'\'\'\'[\w|\s|\d|\(|\)|\{|\}|\[|\]\=|\.|\:|\"|\'|\,]*\'\'\'', 'COMMENT'),
    
    (r'from\s', 'FROM'),
    (r'import\s', 'IMPORT'),
    (r'as\s', 'AS'),
    (r'class\s', 'CLASS'),
    (r'def\s', 'DEF'),
    (r'return\s', 'RETURN'),
    (r'pass', 'PASS'),
    (r'raise\s', 'RAISE'),
    (r'continue\s', 'CONTINUE'),
    (r'break\s', 'BREAK'),
    (r'if\s', ' IF'),
    (r'if\(', ' IF LP'),
    (r'elif', 'ELIF'),
    (r'elif\(', 'ELIF LP'),
    (r'else', 'ELSE'),
    (r'for\s', 'FOR'),
    (r'in\s', 'IN'),
    (r'range', 'RANGE'),
    (r'while\s', 'WHILE'),
    (r'None', 'NONE'),
    (r'True', 'TRUE'),
    (r'False', 'FALSE'),
    (r'not', 'NOT'),
    (r'and', 'AND'),
    (r'\sor\s', 'OR'),
    (r'is\s', 'IS'),
    (r'with\s', 'WITH'),
    (r'print', 'PRINT'),
    #(r'len', 'LEN'),
    (r'str', 'STR'),
    (r'int', 'INT'),
    # (r'float', 'FLOAT'),
    (r'bool', 'BOOL'),
    (r'abs', 'ABS'),
    (r'round', 'ROUND'),
    (r'pow', 'POW'),
    (r'input', 'INPUT'),
    (r'\#.*', 'COMMENT'),
    ('\".*\"', 'STRING'),
    ('\'.*\'', 'STRING'),
    (r'\.', 'WITH_METHOD'),
    (r':', 'COLON'),
    (r'\n', 'NEWLINE'),
    (r' ', 'WHITESPACE'),
    (r'\d+','NUMBER'),
    (r'\d+.+\d','FLOAT'),
    (r'[a-zA-Z_]+[\da-zA-Z_0-9]*','IDENTIFIER'),
    (r'\+','PLUS'),
    (r'\-','MINUS'),
    (r'\*\*','POWER'),
    (r'\*','MULTIPLY'),
    (r'\/','DIVIDE'),
    (r'\[', 'LB'),
    (r'\]', 'RB'),
    (r'\(','LP'),
    (r'\)','RP'),
    (r'==','DOUBLEEQUAL'),
    (r'=','EQUALS'),
    (r'!=', 'NOT_EQUAL'),
    (r',', 'COMA'),
    (r'>=', 'GREATER_OR_EQUAL_THAN'),
    (r'>', 'GREATER_THAN'),
    (r'<=', 'LESS_OR_EQUAL_THAN'),
    (r'<', 'LESS_THAN'),
]