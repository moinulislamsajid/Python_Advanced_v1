def add(a,b): # a and b  are formal Argument or Actual Argument
            #Actual Argument 4 kinds are
            #Position
            #Keyword
            #Default
            #Varibale Length
    c = a+b
    print(c)
#position and keyword
add(40,50)
def position(name,age):
    print(name)
    print(age)
#default
position(age=20,name='sajid')
def default(name,age=20):
    print(name)
    print(age)

default("sajid",22)
#varible length
def varibale_length(a, *b):
   print(a)
   print(b)

varibale_length(20,30,40,50)

def sum(a, *b):
    c = a 
    for i in b:
        c+=i

    print(c)

sum(5,10,15)