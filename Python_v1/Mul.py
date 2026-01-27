from threading import Thread
from time import sleep


class time(Thread):
    def hour(h):
        h = int(input("Enter a Hour : "))
        for i in range(h):
         print(i)
         sleep(1)

            
class time1(Thread):
    def min(m):
        m = int(input("Enter a minaute "))
        for j in range(m):
            print(m)
            sleep(1)

class time2(Thread):
    def sec(s):
       s = int(input("Enter second : "))
       for z in range(z):
         print(s)
         sleep(1)
t1 = time()
t2 = time1()
t3 = time2()

t1.start()
sleep(1)
t2.start()
sleep(1)
t3.start()

t1.join()
t2.join()
t3.join()

