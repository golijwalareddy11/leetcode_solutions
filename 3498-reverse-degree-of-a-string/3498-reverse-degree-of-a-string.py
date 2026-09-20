class Solution:
    def reverseDegree(self, s: str) -> int:
        c=0
        for i in range(len(s)):
                b=(26-(ord(s[i])-ord('a')))
                c+=b*(i+1)
        return c
        