import ply.lex as lex

#SQL LEXER

tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'AND',
    'OR',
    'NOT',
    'IN',
    'IS',
    'NULL',
    'LIKE',
    'BETWEEN',
    'ORDER',
    'BY',
    'ASC',
    'DESC',
    'LIMIT',
    'NUMBER',
    'FLOAT',
    'STRING',
    'ID',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'EQUALS',
    'ASTERISK'
)

t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_AND = r'AND'
t_OR = r'OR'
t_NOT = r'NOT'
t_IN = r'IN'
t_IS = r'IS'
t_NULL = r'NULL'
t_LIKE = r'LIKE'
t_BETWEEN = r'BETWEEN'
t_ORDER = r'ORDER'
t_BY = r'BY'
t_ASC = r'ASC'
t_DESC = r'DESC'
t_LIMIT = r'LIMIT'
t_NUMBER = r'\d+'
t_FLOAT = r'\d+\.\d+'
t_STRING = r'\".*\"'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_EQUALS = r'='
t_ASTERISK = r'\*'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
SELECT * FROM table WHERE id = 1;
'''

lexer.input(data)

while tok := lexer.token():
    print(tok)

