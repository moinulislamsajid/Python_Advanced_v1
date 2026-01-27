#linar search

def search(list,n):
    i = 0
    while i<len(list):
       if list[i] == n:
        return True
    i+=1
    return False


list = [2,3,4,5,6,7,8]
n = 7
if search(list,n):
    print("Ayman Sajid")
else:
    print("No found")