class Solution:
    def findComplement(self, num: int) -> int:
        x=(bin(num)[2:])
        y=""
        for i in x:
            if i=='0':
                y+='1'
            else:
                y+='0'
        return int(y,2)
        