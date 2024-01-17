class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s and t cannot be anagrams if they are not of the same length.
        if len(s) != len(t):
            return False

        # Create a table to hold occurences of s characters.
        occ = [0] * 26

        for c in s:
            occ[ord(c) - ord('a')] += 1

        # Iterate over t and substract its characters occuerences from occ,
        # If we get a negative values in a cell, return False.
        for c in t:
            occ[ord(c) - ord('a')] -= 1
            if occ[ord(c) - ord('a')] < 0:
                return False

        return True
