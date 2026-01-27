#iterstor
nums = [2,5,67,6,4]
it = iter(nums)
print(it.__next__())
print(it.__next__())

class Topten:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 100:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

tot = Topten()
print(next(tot))
for s in tot:
    print(s)


class local_num:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= 50:
            cal = self.num
            self.num += 1
            return cal
        else:
            return StopIteration

lol = local_num()
print(next(lol))
for c in lol:
    print(c)



        

        