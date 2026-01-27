class Studnet:
    school = "Domrakandi"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    




s1 = Studnet(80,75,95)
s2 = Studnet(70,75,90)
print(s1.avg())
print(s2.avg())
    