from  array import *
arr = array('i',[])
n = int(input("Enter the size of array : "))
for i in range(n):
    x = int(input("Enter the value : "))
    arr.append(x)
print(arr)

"""p = int(input("Enter the value of search : "))
l = 0
for j in arr:
    if j==p:
        print(l)
        break
    l+=1
     """
l = int (input("Enter the you wanted to search : "))
g = 0
for f in arr:
    if f==l:
        print(g)
        break
    g+=1
print(arr.index(l))


print(arr.index(l))
