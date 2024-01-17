from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)

        return ans.values()

    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     d = defaultdict(list)

    #     for s in strs:
    #         print(sorted(s))
    #         d[tuple(sorted(s))].append(s)

    #     return d.values()
