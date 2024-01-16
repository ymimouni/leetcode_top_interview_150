from collections import Counter
import re

from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []

        def f(offset, ans):
            W, w = len(words), len(words[0])
            match = '.' * w
            s_list = re.findall(rf'{match}?', s[offset:])
            n = len(s_list)

            count = Counter(words)
            current = count.copy()
            found = 0
            left, right = 0, W

            if right > n:
                return ans

            for i in range(W):
                word = s_list[i]
                if word in count:
                    current[word] -= 1
                    if current[word] < 0:
                        found = 0
                        k = i
                        c = count.copy()
                        while k > 0 and s_list[k] in count and c[s_list[k]] >= 1:
                            found += 1
                            c[s_list[k]] -= 1
                            k -= 1
                    else:
                        found += 1
                else:
                    found = 0

            if found == W:
                ans.append(offset)

            for i in range(W, len(s_list)):
                next_ = s_list[i]
                prev = s_list[i - W]
                if prev in count:
                    current[prev] += 1
                    if found == W:
                        found -= 1
                if next_ in count:
                    current[next_] -= 1
                    if current[next_] < 0:
                        found = 0
                        k = i
                        c = count.copy()
                        while k > 0 and s_list[k] in count and c[s_list[k]] >= 1:
                            found += 1
                            c[s_list[k]] -= 1
                            k -= 1
                    else:
                        found += 1
                    if found == W:
                        ans.append((i + 1 - W) * w + offset)
                else:
                    found = 0

        for offset in range(len(words[0])):
            f(offset, ans)

        return ans
