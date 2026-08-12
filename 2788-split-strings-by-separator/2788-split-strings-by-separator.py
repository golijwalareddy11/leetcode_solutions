class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        a=[]
        for i in words:
            for j in i.split(separator):
                if j!="":
                    a.append(j)
        return a
            
        