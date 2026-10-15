class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        s=[]
        c=0
        for i in range(len(nums)):
            s=[]
            for j in range(i, len(nums)):
                if nums[j] not in s:
                    s.append(nums[j])
                c += len(s) * len(s)
        return c
            


            
        