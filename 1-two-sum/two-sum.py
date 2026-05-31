class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dct = {}
        for i in range(len(nums)):
            diff= target-nums[i] 
            if dct and diff in dct:
                return [i,dct[diff]]
            dct[nums[i]] = i
