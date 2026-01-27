class phone:

    def __init__(self):
        print("I am a phone constructor")
        


    def samsung(self):
        print("World no 1 samart phone company")
        print("Bangladesh No 1 company")


    def iphone(self):
        print("Most wantes phone in the world")
        print("Most highily Price")

    
class Laptop():

    def __init__(self):
        print("i am a Laptop constructor")
        super().__init__()


    def hp(self):
        print("World no 1 samart laptop company")
        print("Bangladesh No 1 company")


    def mac(self):
        print("Most wantesllaptop in the world")
        print("Most highily Price")


class cam(phone,Laptop):
    def __init__(self):
        super().__init__() #constructor call to the first i mean paresent class or super class first
        print("I am a camara constructor")


"""l1 = Laptop()
l1.samsung()
l1.iphone()
l1.hp()
l1.mac()"""
c = cam()