class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        return int(min(len(set(candyType)),n/2))
        