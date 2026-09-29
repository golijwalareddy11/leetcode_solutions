import math 
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        e=0
        o=0
        for i in range(n):
            e+=2*(i+1)
            o+=2*i+1
        return math.gcd(e,o)

        