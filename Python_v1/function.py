def great(n,n1):

       print(n+n1)


#parameters name ar value argument # kono kichu value hocca argument function ar jonna
def look():
    print("Hello world")
    print("Bangladesh")



look()
great(10,20)

#return
def sum_sub(x,y):
    c = x+y
    d = x-y
    return c,d
   

   
vale,vale1= sum_sub(80,40)
print(vale,vale1)


def look(c,d):
    x = c*d
    y = c/d
    return x,y
        # jai somay value return korbo than varibale ar modda rekha than varibale print korbo
        # only return function a use kortah hoi
        # sobsomay variable return korba
        # but oi variable print hoba nah 
        # new varibale function declear kora than oi varibale print kortah hoba 
main,main1 = look(40,20)
print(main,main1)

# docstring
def foll(x,y):
    """This is a python function which is called the general problem of every sucess"""#this is not a comment this is a docstring
    sum = x+y
    return sum


print(foll.__doc__)