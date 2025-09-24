class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dct= Counter(arr)
        maxval= -1
        for i in dct:
            if i==dct[i]:
                maxval = max(maxval,i)
        return maxval