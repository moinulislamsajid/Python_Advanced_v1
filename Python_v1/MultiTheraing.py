


from threading import Thread
from time import sleep


class hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            sleep(1)


class hi(Thread):
     def run(self):
        for i in range(10):
            print("Hi")
            sleep(1)


h = hello()
h1 = hi()

h.start()
sleep(0.2)
h1.start()

h.join()
h1.join()
print("bye")