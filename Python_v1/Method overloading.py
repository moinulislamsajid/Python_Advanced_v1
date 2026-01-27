from xml.etree.ElementTree import XML


class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        s = 0
        if a!=None and b!=None and c!=None:
         s = a+b+c
        elif a!=None and b!=None:
         s = a+b
        else:
            s = a
        return s

    
s1 = student(50,50)
print(s1.sum(30))

class A:
    def show(self):
        print("This is A")
class B(A):
    def look(self):
       print("This is B")



a = B()
a.look()
    
