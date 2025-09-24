class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prevval = 0
        for i in range(1,len(nums)):
            prevval= nums[i-1]%2
            currval= nums[i]%2
            if prevval== currval:
                return False
        return True  