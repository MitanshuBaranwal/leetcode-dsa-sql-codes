class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s= s.split(" ")
        dct1= {}
        dct2= {}

        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] in dct1 and dct1[pattern[i]]!= s[i]:
                return False
            dct1[pattern[i]]= s[i]

        for i in range(len(s)):
            if s[i] in dct2 and dct2[s[i]]!= pattern[i]:
                return False
            dct2[s[i]]= pattern[i]

        return True