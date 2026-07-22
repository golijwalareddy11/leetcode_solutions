class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=nums[0] 
        max_one=nums[0]
        for i in range(1,len(nums)):
            sum=max(nums[i],nums[i]+sum)
            max_one=max(max_one,sum)
        return max_one
        