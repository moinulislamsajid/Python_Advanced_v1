"""def sort(look):
    for i in range(len(look)-1,0,-1):
        for j in range(i):
            if look[j] >  look[j+1]:
                temp = look[j]
                look[j] = look[j+1]
                look[j+1] = temp







look = [233,12,34,56,7,89,9,98,76]
sort(look)
print(look)
"""



def sort(fall):
    for i in range(7):
        minpos = 1
        for j in range(i,8):
            maxpos = j
            if fall[j] < fall[minpos]:
                minpos = j

        temp = fall[j]
        fall[j] = fall[minpos]
        fall[minpos] = temp






fall = [23,45,67,89,23,12,1,44]
sort(fall)
print(fall)