from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = []

        for interval in intervals:
            # If the list of merged intervals is empty or if the current interval
            # does not overlap with the previous one, simply append it.
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                # Otherwise, there is an overlap, so merge the current and the
                # previous intervals.
                res[-1][1] = max(res[-1][1], interval[1])

        return res

#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         def overlap(a: List[int], b: List[int]) -> bool:
#             return a[1] >= b[0]

#         def merge(a: List[int], b: List[int]) -> None:
#             a[1] = max(a[1], b[1])

#         # Sort the list of intervals.
#         intervals.sort()

#         res = []
#         i = 0
#         while i < len(intervals):
#             j = i + 1
#             while j < len(intervals) and overlap(intervals[i], intervals[j]):
#                 merge(intervals[i], intervals[j])
#                 j += 1
#             res.append(intervals[i])
#             i = j

#         return res
