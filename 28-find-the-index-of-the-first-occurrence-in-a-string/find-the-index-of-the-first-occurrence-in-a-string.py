class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_n = len(needle)
        for i in range(len(haystack)+1-len_n):
            if haystack[i:i+len_n]==needle:
                return i
        return -1            