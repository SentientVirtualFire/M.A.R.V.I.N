from marvin.lexer import lexer
from marvin.parser import parse
import matplotlib.pyplot as plt
from os import system
import textwrap 
code = open("main.vin","r").readlines()
print('\033[1;32;40mM.A.R.V.I.N v0.1.0\033[1;34;40m\033[00m')
system("clear")
for i in code:
  if i.startswith(" "):
    i=textwrap.dedent(i)
  if i != "\n" and not i.startswith("//"):
    parse(i)
while True:
  parse(input('\033[1;32;40mM.A.R.V.I.N>\033[1;34;40m\033[00m'))

