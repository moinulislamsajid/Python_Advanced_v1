"""def sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp

num = [21,3,45,67,89,4,90]
sort(num)
print(num)"""
'''from re import M


def sort(lol):
    for i in range(len(lol)):
        for j in range(i):
            if lol[j] > lol[j+1]:
                temp = lol[j]
                lol[j] = lol[j+1]
                lol[j+1] = temp
lol = [44,7,89.100,34,95,90,1000]
sort(lol)
print(lol)'''



from decimal import localcontext


list = [188,345,67,111,23,433,5,778]

local = list.sort()
print(local)

def sort(fol):
    for i in range(len(fol)-1,0,-1):
        for j in range(i):
            if fol[j] > fol[j+1]:
                temp = fol[j]
                fol[j] = fol[j+1]
                fol[j+1] = temp
fol = [12,111,23,45,67,5,444,33]
sort(fol)
print(fol)