class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
       s=set(nums)
       maxc=0
       for i in s:
        if i-1 not in s:
            c=1
            while i+c in s:
                c+=1
            maxc=max(maxc,c)
       return maxc

        