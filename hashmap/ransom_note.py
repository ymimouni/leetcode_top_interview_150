from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        count = Counter(magazine)
        for c in ransomNote:
            if count[c] <= 0:
                return False
            count[c] -= 1

        return True
