class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dct= Counter(nums)
        for i in dct:
            if dct[i]%2!=0:
                return False
        return True