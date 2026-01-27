from curses import LINES
from dis import dis
from pydoc_data.topics import topics
from xxlimited import foo


name = ("sajid","sajid","sakib","sami","rabbi")
name.count("sajid")
print(name)

fool  = ("sajid","sajid","sajid","sajid","sakib","sami","santho") #this is tupels because this value are always fixed try only work on (index number and count number)
fool.count("Sajid")                                                # tuples always started with first braket which is ()
print(fool)

num = (10,10,10,20)
n1 = num.index(20)
print(n1)

s = {20,80,1,5,30,50}
print(s)
#set  not a sequence just print out same value but not at same time
#Distionary
look = {1: 'sajid',2:'sakib', 4 : 'sami'}



keys = ['Navin','Kiran','sajid']
value= ['python','java','js']
data = dict(zip(keys,value))
data['sakib'] = 'c++'
del data['sajid']
print(data)
lol = {"sajid","sakib","sami"}
lol2 = {"arg","brz","ger"}
ch = dict(zip(lol,lol2))
print(ch)


