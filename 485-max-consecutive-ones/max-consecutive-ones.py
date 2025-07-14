class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count= 0
        max_val = 0
        for i in nums:
            if i==1:
                count+=1
            else:
                count= 0
            if count > max_val:
                max_val = count
        return max_val
            