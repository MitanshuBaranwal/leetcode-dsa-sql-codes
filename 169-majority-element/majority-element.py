class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct= {}
        length = len(nums)//2
        for i,j in enumerate(nums):
            print(i,j)
            dct[j] = dct.get(j,0)+1
            if dct[j] >length:
                return j