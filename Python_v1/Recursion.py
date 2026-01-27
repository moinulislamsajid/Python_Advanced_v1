import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i = 0
def firsttime_calls():
    global i
    i+=1
    print("Bangladeah",i)
    firsttime_calls()

firsttime_calls()
