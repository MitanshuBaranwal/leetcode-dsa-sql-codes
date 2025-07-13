class Solution(object):
    def twoSum(self, nums, target):
        diff= 0
        dct= {nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            diff = target - nums[i]
            print(diff)
            if diff in dct.keys() and dct[diff]!=i:
                return [i,dct[diff]]
