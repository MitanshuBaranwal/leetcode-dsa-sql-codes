class Solution:
    def scoreOfString(self, s: str) -> int:
        total_val = 0
        for string in range(1,len(s)):
            total_val += abs(ord(s[string-1]) - ord(s[string]))
        return total_val