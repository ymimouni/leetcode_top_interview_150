from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        papers = [0] * (n + 1)
        for c in citations:
            papers[min(n, c)] += 1

        k = n
        s = papers[n]
        while k > s:
            k -= 1
            s += papers[k]

        return k

    # def hIndex(self, citations: List[int]) -> int:
    #     n = len(citations)

    #     i = 0
    #     citations.sort()
    #     while i < n and i < citations[n - 1 - i]:
    #         i += 1

    #     return i
