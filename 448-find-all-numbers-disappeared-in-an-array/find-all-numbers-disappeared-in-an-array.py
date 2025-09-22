class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        st = set(nums)
        result = []
        for i in range(len(nums)):
            if i+1 not in st:
                result.append(i+1)
        return result

        