#calculator
x = int(input("Enter The First number : "))
op = input("Enter An Operator(+,-,*,/,%) : ")
y = int(input("Enter The Second Number : "))

if op=='+':
    print(x+y)
elif op=='-':
    print(x-y)
elif op=='*':
    print(x*y)
elif op=='/':
    print(x/y)
elif op=='%':
    print(x%y)
else :
    print("invalid Operator")

#mark distrubction
for i in range(5+1):
    mark = int(input("Enter the marks of ant subjects : "))
    if mark>=80:
        print("A+")
    elif mark>=70:
        print("A")
    elif mark>=60:
        print("A-")
    elif mark>=50:
        print("b")
    elif mark>=40:
        print("c")
    elif mark>=33:
        print("d")
    else:
        print("F")