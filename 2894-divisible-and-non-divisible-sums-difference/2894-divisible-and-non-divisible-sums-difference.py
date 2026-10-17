class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        c=0
        d=0
        for i in range(1,n+1):
            if i%m!=0:
                c+=i
            if i%m==0:
                d+=i
        return (c-d)

            
            
        