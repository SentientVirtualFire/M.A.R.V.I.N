from ply import yacc
from lexer import tokens
names = {}
functions = {}
cur_name = ""
if_state = False
if_right_yet = False


def p_statement_assign(p):
  '''statement : NAME EQUAL expression
  | NAME SPACE EQUAL SPACE expression 
  | NAME SPACE EQUAL expression 
  | NAME EQUAL SPACE expression
  | NAME EQUAL statement
  | NAME SPACE EQUAL SPACE statement 
  | NAME SPACE EQUAL statement 
  | NAME EQUAL SPACE statement
  '''
  global cur_name
  if(cur_name != ""):
    if((p[2] == ' ') and (p[4] == ' ')):
      p[5] = str(p[5])
    elif((p[2] == ' ') and (p[4] != ' ')):
      p[4]=str(p[4])
    elif((p[2] != ' ') and (p[3] == ' ')):
      p[4] = str(p[4])
    else:
      p[3] = str(p[3])
    functions[cur_name].append("".join(p[1:]))
  else:
    if((p[2] == ' ') and (p[4] == ' ')):
      names[p[1]] = p[5]
    elif((p[2] == ' ') and (p[4] != ' ')):
      names[p[1]] = p[4]
    elif((p[2] != ' ') and (p[3] == ' ')):
      names[p[1]] = p[4]
    else:
      names[p[1]] = p[3]
    p[0] = p[1]

def p_statement_func(p):
  'statement : NAME LPAREN RPAREN'
  for i in functions[p[1]]:
    parse(i)
  
def p_statement_RCURLY(p):
  'statement : RCURLY'
  global cur_name
  if(cur_name != ""):
    cur_name = ""

def p_statement_create(p):
  'statement : CREATE SPACE NAME LPAREN RPAREN ACTUATE LCURLY'
  global cur_name
  cur_name = p[3]
  functions[cur_name] = []
  print(cur_name)
  p[0] = p[3]

def p_statement_expr(t):
    'statement : NAME'
    global cur_name
    if(cur_name != ""):
      t[0] = t[1]
    else:
      t[0] = names[t[1]]

def p_statement_if(p):
  'statement : IF LPAREN condition RPAREN ACTUATE LCURLY NAME LPAREN RPAREN RCURLY'
  global if_right_yet
  global if_state
  if_state = True
  if(p[3] == True):
    if_right_yet = True
    p[0] = p[7]
  else:
    p[0] = False

def p_statement_elf(p):
  'statement : ELF LPAREN condition RPAREN ACTUATE LCURLY NAME LPAREN RPAREN RCURLY'
  global if_right_yet
  global if_state
  if(if_state == True):
    if(p[3] == True):
      if(if_right_yet == False):
        if_right_yet = True
        p[0] = p[7]
    else:
      p[0] = False
  else:
    print("\033[91mLOGIC error in input! try adding an if at the start")
    p[0] = False

def p_statement_else(p):
  'statement : ELSE LPAREN condition RPAREN ACTUATE LCURLY statement RCURLY'
  global if_right_yet
  global if_state
  if(if_state == True):
    if(p[3] == True):
      if(if_right_yet == False):
        if_right_yet = True
        p[0] = p[7]
      if_state = False
    else:
      p[0] = False
      if_state = False
  else:
    print("\033[91mLOGIC error in input! try adding an if at the start")
    p[0] = False
#works but causes too many conflicts so it is having to sit in the NAUGHT CORNER. THINK ABOUT WHAT YOU HAVE DONE AND STAY THERE FOREVER OR UNTIL I LET U LIVE AGAIN
"""
def p_statement_actuate(p):
  '''statement : statement ACTUATE expression
  | statement ACTUATE statement'''
  if(p[1] == True):
    p[0] = p[3]
  else:
    print(None)
"""


def p_statement_output(p):
  '''statement :  OUTPUT LPAREN expression RPAREN
  | OUTPUT LPAREN statement RPAREN
  | OUTPUT LPAREN condition RPAREN
  '''
  global cur_name
  if(cur_name != ""):
    p[3] = str(p[3])
    functions[cur_name].append("".join(p[1:]))
  else:
    p[0] = p[3]
    print(p[3])
  



def p_statement_true(p):
  '''statement : TRUE'''
  p[0] = True

def p_statement_false(p):
  '''statement : FALSE'''
  p[0] = False

def p_statement_none(p):
  '''statement : NONE'''
  p[0] = None

def p_expression_plus(p):
     '''expression : expression PLUS term
     | statement PLUS expression'''
     p[0] = int(p[1]) + p[3]
 
def p_expression_minus(p):
     'expression : expression MINUS term'
     p[0] = p[1] - p[3]
 
def p_expression_term(p):
     'expression : term'
     p[0] = p[1]
 

 
def p_term_times(p):
     'term : term TIMES factor'
     p[0] = p[1] * p[3]
 
def p_term_div(p):
     'term : term DIVIDE factor'
     p[0] = p[1] / p[3]
 
def p_term_factor(p):
     'term : factor'
     p[0] = p[1]
 


def p_factor_num(p):
     'factor : NUMBER'
     p[0] = p[1]
 
def p_factor_expr(p):
     'factor : LPAREN expression RPAREN'
     p[0] = p[2]

     



"""
MORE THAN PARSE
"""
# MORE, MOREEQUAL,LESSEQUAL,LESS,EQUALEQUAL
def p_condition_morethan(p):
  '''condition : statement MORE statement
  | statement MORE expression
  | expression MORE expression
  
  '''
  try:
    if (type(p[1]) == str) and (type(p[3]) == str):
      p[0] = int(names[p[1]]) > int(names[p[3]])
    elif (type(p[1]) == str) and (type(p[3]) != str):
      p[0] = int(names[p[1]]) > int(p[3])
    else:
      p[0] = int(p[1]) > int(p[3])
  except:
    pass
 



"""
LESS THAN PARSE
"""
def p_condition_lessthan(p):
  '''condition : statement LESS statement
  | statement LESS expression
  | expression LESS expression
  
  '''
  try:
    if (type(p[1]) == str) and (type(p[3]) == str):
      p[0] = int(names[p[1]]) < int(names[p[3]])
    elif (type(p[1]) == str) and (type(p[3]) != str):
      p[0] = int(names[p[1]]) < int(p[3])
    else:
      p[0] = int(p[1]) < int(p[3])
  

  
"""
MORE THAN OR EQUAL TO PARSE
"""
def p_condition_moreThanEqual(p):
  '''condition : statement MOREEQUAL statement
  | statement MOREEQUAL expression
  | expression MOREEQUAL expression
  
  '''
  try:
    if (type(p[1]) == str) and (type(p[3]) == str):
      p[0] = int(names[p[1]]) >= int(names[p[3]])
    elif (type(p[1]) == str) and (type(p[3]) != str):
      p[0] = int(names[p[1]]) >= int(p[3])
    else:
      p[0] = int(p[1]) >= int(p[3])

"""
LESS THAN OR EQUAL TO PARSE
"""
def p_condition_lessThanEqual(p):
  '''condition : statement LESSEQUAL statement
  | statement LESSEQUAL expression
  | expression LESSEQUAL expression
  
  '''
  if (type(p[1]) == str) and (type(p[3]) == str):
    p[0] = int(names[p[1]]) <= int(names[p[3]])
  elif (type(p[1]) == str) and (type(p[3]) != str):
    p[0] = int(names[p[1]]) <= int(p[3])
  else:
    p[0] = int(p[1]) <= int(p[3])
  
def p_condition_EqualEqual(p):
  '''condition : statement EQUALEQUAL statement
  | statement EQUALEQUAL expression
  | expression EQUALEQUAL expression
  
  '''
  if (type(p[1]) == str) and (type(p[3]) == str):
    p[0] = int(names[p[1]]) == int(names[p[3]])
  elif (type(p[1]) == str) and (type(p[3]) != str):
    p[0] = int(names[p[1]]) == int(p[3])
  else:
    p[0] = int(p[1]) == int(p[3])


def p_condition_NotEqual(p):
  '''condition : statement NOTEQUAL statement
  | statement NOTEQUAL expression
  | expression NOTEQUAL expression
  
  '''
  if (type(p[1]) == str) and (type(p[3]) == str):
    p[0] = int(names[p[1]]) != int(names[p[3]])
  elif (type(p[1]) == str) and (type(p[3]) != str):
    p[0] = int(names[p[1]]) != int(p[3])
  else:
    p[0] = int(p[1]) != int(p[3])
  
 # Error rule for syntax errors
def p_error(p):
  if(cur_name == ""):
     print("\033[91mSyntax error in input!")
     print(p.value,"\033[00m")

 # Build the parser
parser = yacc.yacc()
def parse(s):
  while True:
    try:
        s = s
    except EOFError:
        break
    if not s: continue
    parser.parse(s)
    break
    