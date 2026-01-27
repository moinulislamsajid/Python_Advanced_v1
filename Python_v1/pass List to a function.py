def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd

lst = int(input("Enter the evan and odd number : "))
even,odd = count(lst)
print("Even :  {}   and    odd  :   {}".format(even,odd))