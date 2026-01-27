def topten():
  
 u = 1
 while u<=20:
    dd = u*u
    yield dd
    u+=1


total = topten()

for w in total:
    print(w)