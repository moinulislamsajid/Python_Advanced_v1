from os import cpu_count


"""class computer:
    def __init__(self) :
       print("I am a  init")
    def configer(self):
        print("Ram Rom battey camara")

com = computer()
com.configer()
computer.configer(com)"""

"""class computer1:
    def __init__(self,cpu,ram):#constructer
        self.cpu=cpu
        self.ram=ram
    def configer1(self):
        print("Hard disk Memory People",self.cpu,self.ram)
    
com1 = computer1('i5',8)
com2 = computer1('ray5',16)
com1.configer1()
com2.configer1()"""

class slaary:
    def __init__(self,skall,healt):
                self.skall=skall
                self.healt=healt

    def local(self):
        print("This is a methout")
class officer1(slaary):
    def local(self):
     person1 = 5000 * self.skall * self.healt
     print("Officers  Salay : ",person1)

class officer2(officer1):
    def local(self):
     person2 = 2000 * self.skall * self.healt
     print("Step Slaray : ",person2)

con = officer1(40000,3000)
con.local()
con = officer2(2000,500)
con.local()

        
