class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_n = len(needle)
        for i in range((len(haystack)-(len_n))+1):
            print(haystack[i:i+len_n])
            if haystack[i:i+len_n]==needle:
                return i
        return -1            