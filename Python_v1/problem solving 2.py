class Solution:
    def findMedianSortedArrays(self, num1: list[int], num2: list[int]) -> float:
        l = num1+num2
        n=len(l)
        l.sort()
        s=0
        e=n-1
        f=0
        med=0
        if(len(l)%2==0):
            m=int((s+e)/2)
            f=l[m]+l[m+1]
            med=f/2
            return med
        else:
            m=int((s+e)/2)
            f=l[m]
            med=f
            return med