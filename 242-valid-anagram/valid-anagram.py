class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct1 = Counter(s)
        dct2 = Counter(t)
        return dct1 == dct2