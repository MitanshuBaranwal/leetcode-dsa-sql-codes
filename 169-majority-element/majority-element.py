class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct= Counter(nums)
        length= len(nums)//2
        for i in dct.keys():
            if dct[i] > length:
                return i