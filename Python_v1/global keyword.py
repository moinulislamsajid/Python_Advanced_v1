#socpe
#function ar opora varible called deala sati global variable
#function ar modda deala sati local varibale 

a =50  #this is a gloabal varibale 
print(id(a))
def sometimes():
    global a
    a = 10
     #this is a local varibale

    #x = globals()['a']
    #print(id(x))
  



sometimes()
print(a)




print(a)