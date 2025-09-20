class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        dct= {}
        dct2= {}
        for i in range(len(s)):
            if s[i]in dct and dct[s[i]]!=t[i]:
                return False
            if t[i]in dct2 and dct2[t[i]]!=s[i]:
                return False
            dct[s[i]] = t[i]
            dct2[t[i]] = s[i]
        return True
