class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        s=""
        if sum == 0 or sum > 9 * num:
            return ""
        for i in range(num):
            d = min(9, sum)
            s += str(d)
            sum -= d
        return s


    


        