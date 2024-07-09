from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital, profits))
        projects.sort()

        h = []
        p = 0
        while k > 0:
            while p < len(capital) and projects[p][0] <= w:
                heapq.heappush(h, -projects[p][1])
                p += 1

            if not h:
                break

            w += -heapq.heappop(h)
            k -= 1

        return w
