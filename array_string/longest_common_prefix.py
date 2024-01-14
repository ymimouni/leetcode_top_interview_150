from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ''
        elif n == 1 or not strs[0]:
            return strs[0]

        ans = []
        stop = False
        ptr = 0

        while not stop:
            for i, s in enumerate(strs):
                if i == 0 and len(s) > ptr:
                    c = s[ptr]
                elif ptr >= len(s) or s[ptr] != c:
                    stop = True
                    break
                elif i == len(strs) - 1:
                    ans.append(c)
                    ptr += 1

        return ''.join(ans)
