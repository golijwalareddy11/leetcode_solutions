class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l=list(zip(heights,names))
        l.sort(reverse=True)
        return [i[1] for i in l]