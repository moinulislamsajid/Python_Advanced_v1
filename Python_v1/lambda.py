#function without name is called lambda
from cgitb import reset
from traceback import print_tb
from unittest import result


num1 = 10
num2 = 30
print(num2  if num2>num1 else num1)

f = lambda a,b : a*b
result = f(5,10)
print(result)



t = lambda  g,h:g/h
result1 = t(50,10)
print(result1)
