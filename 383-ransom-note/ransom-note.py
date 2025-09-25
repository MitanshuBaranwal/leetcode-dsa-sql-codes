class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNotedct= Counter(ransomNote)
        magazinedct= Counter(magazine)
        for i in ransomNotedct:
            print(i)
            if i not in magazinedct or ransomNotedct[i] > magazinedct[i]:
                print(ransomNotedct[i])
                print(magazinedct[i])
                return False
        return True