class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dct = dict()
        for i,j in enumerate(nums):
            diff = target - j
            if diff in dct.keys():
                return [dct[diff],i]
            dct[j] = i
