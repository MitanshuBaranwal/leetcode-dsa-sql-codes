class Solution(object):
    def twoSum(self, nums, target):
        dct = dict()
        for i,j in enumerate(nums):
            if dct.keys() and target-j in dct.keys():
                return [dct[target-j],i]
            dct[j] = i

