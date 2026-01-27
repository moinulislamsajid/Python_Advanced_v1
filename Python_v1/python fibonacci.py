def fib(n):
    a = 0
    b = 1
  
    if n==a:
        print(a)

    else:
        print(a)
        print(b)
        for i in range(2,n):
           s=a+b
           a=b
           b=s
           print(s)
fib(n=int(input("Enter the number : ")))


