class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        x = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                x += i
                if i != num // i:
                    x += num // i
        if x == num:
            return True
        return False