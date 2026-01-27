class cars():
    def __init__(self):
        self.milg= 20
        self.com = "BMW"

    def compare(self,look):
        if self.milg == look.milg:
            return True
        else:
            return False

    def compare1(self,look1):
        if self.com == look1.com:
            return True
        else:
            return False
            

c1 = cars()
c2 = cars()
c1.milg = 20
c2.com = "BMW"
if c1.compare(c2):
    print("They are Mil Quaal",c1.milg)
else:
    print("Not Equal")
if c1.compare1(c2):
    print("They are company Quaal",c2.com)
else:
    print("Not Equal")

print(c1.milg)
print(c2.com)
    
