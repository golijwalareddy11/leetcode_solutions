class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor=0
        nonzero=False
        for i in nums:
            xor=xor^i
            if i!=0:
                nonzero=True
        if xor!=0:
            return len(nums)
        if nonzero:
            return len(nums)-1
        else:
            return 0
        