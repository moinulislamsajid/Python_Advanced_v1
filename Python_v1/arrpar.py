from array import array



#lok = array('i',[2,3,4,5,6,7,8,9])
#fol = array('u',['a','s','f','g'])
#print(fol)



fol = array('i',[2,3,4,5,6,7,8,9])
fol1 = array(fol.typecode,(g*g for g in fol))
for j in fol1:
   print(j)

lol = array('i',[9,7,6,5,4])
tol = array(lol.typecode,(h*h*h for h in lol))
g = 0
while g<len(tol):
    print(tol[g])
    g+=1

nol = array('i',[23,2,45,67,89])
bol = array(nol.typecode,(j*j for j in nol))
q = 0
while q<len(bol):
    print(bol[q])
    q+=1
vol = array('f',[23,45,67,89,76,54],'i')
print(vol)