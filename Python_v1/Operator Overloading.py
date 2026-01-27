from this import d


class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __sub__(self,other):  #overloading
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        s3 = student(m1,m2)
        return s3

    """def __gt__(self,other):#operator overloading
        r1 = self.m1 + other.m1
        r2 = self.m2 + other.m2
        if r1>r2:
            return True
        else:
            return False"""

    def __lt__(self,other):
        r1 = self.m1 + other.m1
        r2 = self.m2 + other.m2
        if r1<r2:
            return False
        else:
            return True

s1 = student(50,50)
s2 = student(100,101)

s3 = s1 - s2
print(s3)
if s1<s2:
    print("S2 Wins here")

else:
    print("S1 wins here" )