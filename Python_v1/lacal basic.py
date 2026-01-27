#varible address
from re import L, X
from unicodedata import decimal


num = 10
print(id(num))
name = "sajid"
print(id(name))

a = 10
b = a 
print(id(a))
print(id(b))
print(id(10))
#dtat type
n = 10
print(type(n))
num = 3+3j
print(type(num))
print()

d= {"sajid" : "samsung","sakib" :"iphone", "sami" : "oneplus" }
print(d) 
print(d.keys())
print(d.values())
print(d["sajid"])
#operation
print(bin(25))
print(oct(0b11111))
#print(decimal(0b10101010))
#swap
x = 20
y = 30
#x,y=y,x
x = x+y
y = x-y
x = x-y


print("X : ",x)
print("Y : ",y)