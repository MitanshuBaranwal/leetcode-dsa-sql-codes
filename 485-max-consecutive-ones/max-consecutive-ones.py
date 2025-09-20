class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxval= 0
        maxcurr= 0
        for i in range(0,len(nums)):
            if nums[i]== 0:
                maxcurr= 0
            else:
                maxcurr+=1
                maxval= max(maxcurr,maxval)
        return maxval