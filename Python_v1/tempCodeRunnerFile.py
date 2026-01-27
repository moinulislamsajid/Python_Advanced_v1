pos = -1
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
    print("Not Found")