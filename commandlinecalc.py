import math
import numpy

def Add(a, b):
  return a + b

def Sub(a, b):
  return a - b

def Mul(a, b):
  return a * b

def Div(a, b):
  return a / b

go = 1

while go == 1:
  print('\033c')
  print('[1] Addition')
  print('[2] Subtraction')
  print('[3] Muliplication')
  print('[4] Division')
  print()
  choice = input('Choose one of the above: ')
  if choice == 1:
    a = input('First number: ')
    b = input('Second number: ')
    print(Add(a, b))
  elif choice == 2:
    a = input('First number: ')
    b = input('Second number: ')
    print(Sub(a, b))
  elif choice == 3:
    a = input('First number: ')
    b = input('Second number: ')
    print(Mul(a, b))
  elif choice == 4:
    a = input('First number: ')
    b = input('Second number: ')
    print(Div(a, b))
  else:
    print('That is not a choice.')
  
  go = input('Type 1 to try again and anything else to stop: ')

exit()
