class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        a=0
        for i in range(len(s)):
            d={}
            for j in range(i,len(s)):
                d[s[j]]=d.get(s[j],0)+1
                if (d[s[j]])>2:
                    break
                a=max(a,j-i+1)
        return a
        