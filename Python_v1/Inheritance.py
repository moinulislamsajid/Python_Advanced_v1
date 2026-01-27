class A:
    def features1(self):

        print("Feature 1 working")


    def features2(self):
        print("Feature 2 is working")
class B(A):
    def features3(self):

        print("Feature 3 working")


    def features4(self):
        print("Feature 4 is working")

a1 = B()
a1.features1()
a1.features2()
a1.features3()
a1.features4()