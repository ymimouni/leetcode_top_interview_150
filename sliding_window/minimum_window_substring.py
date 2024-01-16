from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)

        c_count = Counter(t)
        c_remaining = c_count.copy()
        ans = 0, float("inf")

        l, r = 0, 0
        c_found = 0
        excess_char = False

        for r, c in enumerate(s):
            if c in c_count:
                if c_remaining[c] >= 1:
                    c_found += 1
                c_remaining[c] -= 1

            while l <= r and c_found == m:
                if c_found == m and r - l < ans[1] - ans[0]:
                    ans = l, r
                leftmost_c = s[l]
                if leftmost_c in c_count:
                    if c_remaining[leftmost_c] == 0:
                        c_found -= 1
                    c_remaining[leftmost_c] += 1
                l += 1

        return s[ans[0]: ans[1] + 1] if ans[1] != float("inf") else ""
