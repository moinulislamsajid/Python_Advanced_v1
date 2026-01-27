x = int(input("Enter the remain time to save the string : "))
i = 1
while i<=x:
    print("candy",i)
    i+=1

a = int(input("How many candy you needed : "))
av_canday = 20
d = 1
while d<=a:
    if a>av_canday:
        print("Sorry Out of Stoks")
        print("Now Available Candy",av_canday)
        break
    print("candy",d)
    d+=1
#continue

for i in range(1,100):
    if i%3==0:
        print(i)
    i+=1

print("bye")