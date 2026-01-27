from textwrap import shorten
from unicodedata import name


class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    def show(self):
        print(self.name , self.rollno)
        self.lap.show()

class laptop:
    def __init__(self):
        self.brand = "Hp"
        self.cpu = "i5"
        self.ram = 8
    def show(self):
        print(self.brand , self.cpu , self.ram)
    

s1 = student("Sajid",20)
s2 = student("sakib",50)

s1.show()