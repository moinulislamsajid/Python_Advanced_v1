'''pos = -1
def search(list,n):
    l = 0
    u = len(list)-1
    while l<=u:
        mid = (l+u) // 2
        if list[mid] == n:
            globals()['pos'] = mid

        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid - 1





list = [23,34,56,78,98,23,45]
n = 23
if search(list,n):
    print("Fonud at ",pos+1)
else:
    print("Not Found")'''
pos = -1
def search(list,n):
    f = 0
    l = len(list) - 1
    while f<=l:
        mid = (f+l) // 2
        if list[mid] == n:
            globals()['pos'] = mid
        else:
            if list[mid] < n:
                f = mid + 1

            else:
                l = mid -1




list = [28,23,45,223,4,56]
n = 223

if search(list,n):
    print("Found At ",pos+1)

else:
    print("Not Founded")



pos = -1
def local(look,t):
    g = 0
    h = len(look) -1
    while g <= h:
        mid = (g+h) //2
        if look[mid] == n:
            globals()['pos'] = mid


        else:
            if look[mid] < n:
                g = mid+1

            else:
                h = mid-1






look = [12,12,34,34,24]
t = 43
if local(look,t):
    print("Found at",pos+1)
else:
    print("Not found")