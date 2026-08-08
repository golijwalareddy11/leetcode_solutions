class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        if n==1 :
            return True
        while n!=1:
            if n in a:
                return False
            a.add(n)
            x=str(n)
            s=0
            for i in x:
                s+=int(i)**2
            n=s
        return True
            

        