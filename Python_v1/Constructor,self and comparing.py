#constructer
#self
#any things do not pass the class when use the pass keyword
class computer:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    
    def comppare(self,other):
        if self.age == other.age:
            return True
        else:
            False
    def compile(self,any):
        if self.name == any.name:
            return True
        else:
            return False

c1 = computer('sajid',20)
c1.age = 20
#c1.age = 20
#c2 = computer('sajid',20)
#c1.name = "Ayman Sajid"
'''if c1.comppare(c2):
    print("They are Same")
else:
    print("They ara not same")
if c1.compile(c2):
    print("The name is same",c1.name)
else:
    print("Not equal the name")


print(c1.name)
print(c2.age)'''