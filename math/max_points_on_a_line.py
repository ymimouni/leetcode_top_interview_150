from typing import List


from collections import defaultdict
from math import atan2


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 1

        for i in range(n - 1):
            cnt = defaultdict(int)
            for j in range(i + 1, n):
                cnt[atan2(
                    points[j][1] - points[i][1],
                    points[j][0] - points[i][0]
                )] += 1
                cnt[atan2(
                    -points[j][1] + points[i][1],
                    -points[j][0] + points[i][0]
                )] += 1
            res = max(res, max(cnt.values()) + 1)

        return res
