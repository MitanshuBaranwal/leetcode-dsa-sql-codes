class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        st = set()
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                st.add(1)
            elif nums[i] < nums[i-1]:
                st.add(-1)
        return len(st) <= 1