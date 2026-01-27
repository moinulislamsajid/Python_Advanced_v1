# 3 functioon
#map
#reduce
#filter
from functools import reduce


def is_function(n):
    return n%2==0
nums = [20,22,24,28,21,23,25]
even = list(filter(is_function,nums))
print(even)



def local_even(x):
    return x%2==0
    
nums = [2,4,6,8,9,11,13,15]
hey = list(filter(local_even,nums))
print(hey)

#lambda
people = [30,33,34,36,37,39,40,42,44]
look_even = list(filter(lambda n : n%2==0,people))#lambda next varibale name : than condition #always remember always called list
doubles = list(map(lambda n : n+2,look_even))
print(doubles)
sum = reduce(lambda a,b : a+b,doubles)#reduce a list none likha laga nah list lekha laga nah
print(sum)
sub = reduce(lambda g,h : g-h,doubles)
print(sub)
#to change the value to use in Map


