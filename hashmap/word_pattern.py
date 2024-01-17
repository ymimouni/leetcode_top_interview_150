class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split()
        if len(pattern) != len(list_s):
            return False

        map_p_s = {}
        map_s_p = {}
        for c, w in zip(pattern, list_s):
            if c not in map_p_s and w not in map_s_p:
                map_p_s[c] = w
                map_s_p[w] = c
            elif map_p_s.get(c) != w:
                return False

        return True
