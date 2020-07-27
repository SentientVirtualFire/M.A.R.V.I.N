from marvin.lexer import lexer
from marvin.parser import parse
code = open("main.vin","r").readlines()
lexer.input("'hello there' check")
print('\033[1;32;40mM.A.R.V.I.N v0.1.0\033[1;34;40m\033[00m')
types = []

while True:
  tok = lexer.token()
  if not tok:
    break
  print(tok)
  types.append(tok.type)

for i in code:
  parse(i)

while True:
  parse(input('\033[1;32;40mM.A.R.V.I.N>\033[1;34;40m\033[00m'))
  print()