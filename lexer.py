from ply import lex

reserved_tokens={
  'if' : 'IF',
  'else':'ELSE',
  'for':'FOR',
  'while':'WHILE',
  'create':'CREATE',
  'elf':'ELF',
  'two':'TWO',
  'mod':'MOD',
  'int':'INT',
  'flt':'FLOAT',
  'str':'STR',
  'lst':'LST',
  'dct':'DCT',
  'comb':'COMB',
  'true':'TRUE',
  'false':'FALSE',
  'none':'NONE',
  'output':'OUTPUT',
  'return':'RETURN'
}
tokens = list(reserved_tokens.values())+[
    'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN','NAME','ACTUATE','EQUAL','LCURLY','RCURLY','COMMENT','QUOTE','SPACE','NEWLINE','LESS','MORE','LESSEQUAL','MOREEQUAL','EQUALEQUAL','NOTEQUAL'
]
t_LCURLY  = R'\{'
t_RCURLY  = R'\}'
t_ACTUATE = r'=>'
t_EQUAL   = r'='
t_LESS = r'<'
t_MORE = r'>'
t_LESSEQUAL = r'<='
t_MOREEQUAL = r'>='
t_EQUALEQUAL = r'=='
t_NOTEQUAL = r'!='
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COMMENT = r'//'
t_QUOTE = '\'|"'
t_SPACE = r'[ ]'
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved_tokens:
        t.type = reserved_tokens[t.value]
    else:
        t.type = 'NAME'
    return t


def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print(f"Integer value too large: {t.value}")
        t.value = 0
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character {t.value[0]!r} on line {t.lexer.lineno}")
    t.lexer.skip(1)

t_ignore = '//'

lexer = lex.lex()