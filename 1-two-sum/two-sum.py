class Solution(object):
    def twoSum(self, nums, target):
        dct = dict()
        for i,j in enumerate(nums):
            diff = target-j
            if dct.keys() and diff in dct.keys():
                return [dct[diff],i]
            dct[j] = i

