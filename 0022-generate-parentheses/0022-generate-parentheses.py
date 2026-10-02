class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        c=[]
        def generate(s,open,close):
            if len(s)==2*n:
                c.append(s)
                return
            if open<n:
                generate(s+"(",open+1,close)
            if close<open:
                generate(s+")",open,close+1)
        generate("",0,0)
        return c                  