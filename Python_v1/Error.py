# error
# 3 kinds of error
# compile time
# logical error
# run time error
a = 5
b = 0
try:
    print("resourse open")
    print(a/b)
    f = int(input("enter a number : "))
    print(f)
except ZeroDivisionError as e:
    print("Hey you cannot be divide a number by zero",e)
except ValueError as e:
    print("Invalid input")
except Exception as e:
    print("somethinng went wrong ")
finally:
    print("resourse close")

