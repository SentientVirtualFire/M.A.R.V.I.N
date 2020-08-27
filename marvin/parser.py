from ply import yacc
from marvin.lexer import tokens
import importlib
from random import randint
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from math import sqrt
from .physics import *
circles = []

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 50), ylim=(0, 50))


def change_circle_color(circle,colour):
  x,y = circle.center
  circle1 = plt.Circle((x,y),radius=1, color=colour)
  ax.add_artist(circle1)
  return circle1

def circle(radius,center,colour=None,save=None):
  circle1 = plt.Circle(center,radius=radius, color=colour)
  ax.add_artist(circle1)
  circles.append(circle1)
  if save!=None:
    plt.savefig(save)

def title(title,fontsize):
  plt.title(title, fontsize=fontsize)

def xlen(start,end):
  plt.xlim(start,end)

def ylen(start,end):
  plt.ylim(start,end)

def fancy():
  from seaborn import set
  set()

def reveal():
  plt.show()

# circle(0.1,(randint(1,5),randint(1,5)))
# circle(0.1,(randint(1,5),randint(1,5)))

"""def animate(i):
    for i in range(len(circles)):
      x,y = circles[i].center
      circles[i].center = (x+randint(-1,1)/10,y+randint(-1,1)/10)
    return circles

anim = animation.FuncAnimation(fig, animate, 
                               frames=360, 
                               interval=20,
                               blit=True)

plt.show()
"""
"""
dont use this
just look at it and admire how not noice
class graphing:
  def __init__(sea=True):
    if(sea == True):
      
"""
names = {}
functions = {}
cur_name = ""
if_state = False
if_right_yet = False
string_state = False
string_itself = ""
for_state = False
for_block = {"code":[]}
imports = ""
error_state=False
circle_names = {}
physics=False
circle_touches={}
def animate(v):
    global circles
    global names
    circles[1].color = (255,255,0)
    for i in functions['animate']['code']:
      parse(i)
    if physics == True:
      for i in range(len(circles)-1):
        circles[i].center = frame(circles[i])
        for v in range(len(circles)):
          if i!=v:
            if(collision(circles[i],circles[v]) == True):
              key_list = list(circle_names.keys())
              names['nowTouched'] = key_list[v]
              try:
                parse(circle_touches[key_list[i]]["ontouch"])
                x,y = circles[v].center
                circles[v].center = (x+2,y+2)
              except:
                x,y = circles[v].center
                circles[v].center = (x+2,y+2)
    return circles


def p_statement_touch(p):
  'statement : TOUCH SPACE NAME ACTUATE statement'
  circle_touches[p[3]]['onTouch'] = p[5]
def p_statement_changecolor(p):
  'statement : CLR SPACE NAME argumentr'
  if(for_state == True):
    p[4] = p[4][2]
    for_block["code"].append("".join(p[1:]))
  elif(cur_name != ""):
    p[4] = p[4][2]
    functions[cur_name]["code"].append("".join(p[1:]))
  else:
    colours = p[4][0]
    circles[circle_names[p[3]]] = change_circle_color(circles[circle_names[p[3]]],(int(colours[0])/255,int(colours[1])/255,int(colours[2])/255))
    p[4] = p[4][2]
    p[0]="".join(p[1:])


def p_statement_circle(p):
  'statement : CIRCLE SPACE NAME EQUAL argumentr'
  if(for_state == True):
    p[5] = p[5][2]
    for_block["code"].append("".join(p[1:]))
  elif(cur_name != ""):
    p[5] = p[5][2]
    functions[cur_name]["code"].append("".join(p[1:]))
  else:
    try:
      if(circle_names[p[3]] > -1):
        x,y = circles[circle_names[p[3]]].center
        circles[circle_names[p[3]]].center = ((x+int(p[5][0][0])/10),(y+int(p[5][0][1])/10))
      else:
        circle(1,(int(p[5][0][0]),int(p[5][0][1])))
        circle_names[p[3]] = len(circles)-1
    except:
      circle(1,(int(p[5][0][0]),int(p[5][0][1])))
      circle_names[p[3]] = len(circles)-1
      p[5] = p[5][2]
      p[0]="".join(p[1:])
def p_statement_randmove(p):
  'statement : RAND SPACE NAME'
  if(for_state == True):
    for_block["code"].append("".join(p[1:]))
  elif(cur_name != ""):
    functions[cur_name]["code"].append("".join(p[1:]))
  else:
    x,y = circles[circle_names[p[3]]].center
    circles[circle_names[p[3]]].center = ((x+(randint(1,10)-randint(1,10))/10),(y+(randint(1,10)-randint(1,10))/10))
    p[0]="".join(p[1:])
def p_statement_reveal(p):
  'statement : REV LPAREN RPAREN'
  reveal()
  p[0]="".join(p[1:])
def p_statement_start(p):
  'statement : START LPAREN RPAREN'
  print(functions['animate'])
  anim = animation.FuncAnimation(fig, animate, frames=360,interval=20,blit=True)
  plt.show()
  p[0] = p[3]
  
def p_statement_assign(p):
  '''statement : NAME EQUAL expression
  | NAME SPACE EQUAL SPACE expression 
  | NAME SPACE EQUAL expression 
  | NAME EQUAL SPACE expression
  | NAME EQUAL statement
  | NAME SPACE EQUAL SPACE statement 
  | NAME SPACE EQUAL statement 
  | NAME EQUAL SPACE statement
  | NAME EQUAL condition
  '''
  global cur_name
  global for_block
  global for_state
  if(for_state == True):
    if((p[2] == ' ') and (p[4] == ' ')):
      p[5] = str(p[5])
    elif((p[2] == ' ') and (p[4] != ' ')):
      p[4]=str(p[4])
    elif((p[2] != ' ') and (p[3] == ' ')):
      p[4] = str(p[4])
    else:
      p[3] = str(p[3])
    for_block["code"].append("".join(p[1:]))
  elif(cur_name != ""):
    if((p[2] == ' ') and (p[4] == ' ')):
      p[5] = str(p[5])
    elif((p[2] == ' ') and (p[4] != ' ')):
      p[4]=str(p[4])
    elif((p[2] != ' ') and (p[3] == ' ')):
      p[4] = str(p[4])
    else:
      p[3] = str(p[3])
    functions[cur_name]["code"].append("".join(p[1:]))
  else:
    if((p[2] == ' ') and (p[4] == ' ')):
      names[p[1]] = p[5]
    elif((p[2] == ' ') and (p[4] != ' ')):
      names[p[1]] = p[4]
    elif((p[2] != ' ') and (p[3] == ' ')):
      names[p[1]] = p[4]
    else:
      names[p[1]] = p[3]
    p[3] = str(p[3])
    p[0]="".join(p[1:])

def p_statement_funcNoArg(p):
  '''statement : NAME LPAREN RPAREN
  | NAME argumentr'''
  try:
    if p[2][1] == "argr":
      for i in range(len(p[2][0])):
        names[functions[p[1]]["args"][i]] = p[2][0][i]
      for i in functions[p[1]]["code"]:
        parse(i)
  except:
    for i in functions[p[1]]["code"]:
      parse(i)

def p_statement_RCURLY(p):
  'statement : RCURLY'
  global cur_name
  global for_state
  if for_state == True:
    for_state = False
    for v in range(for_block["range"]):
      names[for_block["var"]] +=1
      for i in for_block["code"]:
        parse(i)
  elif(cur_name != ""):
    cur_name = ""

def p_statement_create(p):
  '''statement : CREATE SPACE NAME LPAREN RPAREN ACTUATE LCURLY
  | CREATE SPACE NAME argument ACTUATE LCURLY'''
  global cur_name
  try:
    if p[4][1] == "arg":
      cur_name = p[3]
      functions[cur_name] = {"code":[],"args":p[4][0]}
      p[0] = p[3]
    else:
      cur_name = p[3]
      functions[cur_name] = {"code":[],"args":[]}
      p[0] = p[3]
  except:
    cur_name = p[3]
    functions[cur_name] = {"code":[],"args":[]}
    p[0] = p[3]
    
def p_statement_expr(t):
    'statement : NAME'
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
    exit()
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
    exit()
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

def p_expression_string(p):
  '''expression : STRING
  '''
  p[0] = p[1]

def p_statement_output(p):
  '''statement :  OUTPUT argumentr
  | OUTPUT argument 
  '''
  global cur_name
  global for_state
  global for_block
  if p[2][1] == 'argr':
    if(for_state == True):
      for_block["code"].append("".join(p[1])+p[2][2])
    elif(cur_name != ""):
      functions[cur_name]["code"].append("".join(p[1])+p[2][2])
    else:
      p[0] = p[2][0]
      for i in range(len(p[2][0])):
        p[2][0][i] = p[2][0][i][1:-1]  
      print("".join(p[2][0]).replace('"',""))
  else:
    if(for_state == True):
      for_block["code"].append("".join(p[1])+p[2][2])
    elif(cur_name != ""):
      functions[cur_name]["code"].append("".join(p[1])+p[2][2])
    else:
      p[0] = p[2][0]
      print(names[p[2][0][0]])
  
def p_statement_physics(p):
  'statement : PHYS LPAREN RPAREN'
  global physics
  physics = True
  p[0] = "you found me. The egg. I have been impisoned in here since the (g)od of randomness THE MIGHTY EGG left me here. Done leave me... no... DONT GO AWAY... WHY!!!"


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
     | statement PLUS expression
     | expression PLUS expression'''
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
 
def p_term_uminus(p):
  'term : MINUS term'
  p[0] = -1 * p[2]

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
  except:
    pass

  
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
  except:
    pass

"""
LESS THAN OR EQUAL TO PARSE
"""
def p_condition_lessThanEqual(p):
  '''condition : statement LESSEQUAL statement
  | statement LESSEQUAL expression
  | expression LESSEQUAL expression
  
  '''
  try:
    if (type(p[1]) == str) and (type(p[3]) == str):
      p[0] = int(names[p[1]]) <= int(names[p[3]])
    elif (type(p[1]) == str) and (type(p[3]) != str):
      p[0] = int(names[p[1]]) <= int(p[3])
    else:
      p[0] = int(p[1]) <= int(p[3])
  except:
    pass
  
def p_condition_EqualEqual(p):
  '''condition : statement EQUALEQUAL statement
  | statement EQUALEQUAL expression
  | expression EQUALEQUAL expression
  
  '''
  try:
    if (type(p[1]) == str) and (type(p[3]) == str):
      p[0] = int(names[p[1]]) == int(names[p[3]])
    elif (type(p[1]) == str) and (type(p[3]) != str):
      p[0] = int(names[p[1]]) == int(p[3])
    else:
      p[0] = int(p[1]) == int(p[3])
  except:
    pass

def p_condition_NotEqual(p):
  '''condition : statement NOTEQUAL statement
  | statement NOTEQUAL expression
  | expression NOTEQUAL expression
  
  '''
  try:
    if (type(p[1]) == str) and (type(p[3]) == str):
      p[0] = int(names[p[1]]) != int(names[p[3]])
    elif (type(p[1]) == str) and (type(p[3]) != str):
      p[0] = int(names[p[1]]) != int(p[3])
    else:
      p[0] = int(p[1]) != int(p[3])
  except:
    pass
  


def p_expression_list(p):
  'expression : LIST'
  p[1] = p[1][1:-1].split(",")
  for i in range(len(p[1])):
      try:
        p[1][i] = int(p[1][i])
      except:
        p[1][i] = p[1][i][1:-1]
  p[0] = p[1]



def p_argument_args(p):
  'argument : ARGS'
  raw = p[1]
  p[1] = p[1][1:-1].split(",")[:-1]
  for i in range(len(p[1])):
      p[1][i] = p[1][i]
  p[0] = [p[1],'arg',raw]



def p_argumentr_args(p):
  'argumentr : ARGSR'
  raw = p[1]
  p[1] = p[1][1:-1].split(",")[:-1]
  for i in range(len(p[1])):
    try:
        p[1][i] = int(p[1][i])
    except:
        p[1][i] = p[1][i]
  p[0] = [p[1],'argr',raw]



def p_statement_for(p):
  'statement : FOR LPAREN statement SEMI NUMBER RPAREN ACTUATE LCURLY'
  global for_state
  global for_block
  for_state = True
  for_block["range"] = p[5]
  for_block["var"] = p[3]


def p_statement_modpy(p):
  'statement : MODPY SPACE expression'
  global imports
  imports = importlib.import_module(p[3][1:-1])

def p_statement_mod(p):
  'statement : MOD SPACE expression'
  code = open(p[3][1:-1]+".vin","r").readlines()
  for i in code:
    if type(i) != None and i != "" and not i.startswith("//"):
      parse(i)


def p_statement_pyfunc(p):
  '''statement : HASH NAME LPAREN RPAREN
  | HASH NAME argumentr'''
  try:
    if(p[3][1] == 'argr'):
      for i in range(len(p[3][0])):
        p[3][0][i] = p[3][0][i].replace('"',"")
      getattr(imports,p[2])(*p[3][0])
    else:
      getattr(imports,p[2])()
  except:
    getattr(imports,p[2])()


 # Error rule for syntax errors
#'''
def p_error(p):
  if(cur_name == ""):
    try:
      print("\033[91mSyntax error in input!")
      print(p,"\033[00m")
      exit()
      #error_state = True OkokokokokokokOKOKOKOK
    except:
      print("\033[91mGOOD JOB WE NOW HAVE AN ERROR AGAINST OURSELVES. MARVIN IS SELF DESTRUCTING IN 3..2..1.. BOOM\033[00m")
      exit()
#'''



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
    
