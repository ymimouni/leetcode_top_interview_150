from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        def overlap(interval1, interval2):
            return max(interval1[0], interval2[0]) <= min(interval1[1], interval2[1])

        def merge_intervals(interval1, interval2):
            return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

        def insert_interval(intervals, new_interval):
            left, right = 0, len(intervals) - 1
            while left <= right:
                pivot = (left + right) // 2
                if new_interval[0] < intervals[pivot][0]:
                    right = pivot - 1
                else:
                    left = pivot + 1
            i = left - 1
            while i >= 0 and overlap(intervals[i], new_interval):
                i -= 1
            return i + 1

        insert_pos = insert_interval(intervals, new_interval)

        answer = intervals[:insert_pos]
        i = insert_pos
        curr_interval = new_interval
        while i < len(intervals) and overlap(curr_interval, intervals[i]):
            curr_interval = merge_intervals(curr_interval, intervals[i])
            i += 1
        answer.append(curr_interval)

        answer += intervals[i:]

        return answer

    # def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    #     def overlap(interval1, interval2):
    #         return max(interval1[0], interval2[0]) <= min(interval1[1], interval2[1])

    #     def merge_intervals(interval1, interval2):
    #         return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

    #     def insert_interval(intervals, new_interval):
    #         i = 0
    #         while i < len(intervals) and new_interval[0] > intervals[i][0]:
    #             i += 1
    #         return intervals[:i] + [new_interval] + intervals[i:]

    #     intervals = insert_interval(intervals, new_interval)

    #     n = len(intervals)

    #     answer = []
    #     i = 0
    #     while i < n:
    #         curr_interval = intervals[i]
    #         while i < n and overlap(curr_interval, intervals[i]):
    #             curr_interval = merge_intervals(curr_interval, intervals[i])
    #             i += 1
    #         answer.append(curr_interval)

    #     return answer

    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     def overlap(interval1, interval2):
    #         return max(interval1[0], interval2[0]) <= min(interval1[1], interval2[1])

    #     n = len(intervals)
    #     if n == 0:
    #         return [newInterval]

    #     ans = []
    #     i = 0
    #     newI_added = False
    #     while i < n:
    #         if overlap(intervals[i], newInterval):
    #             while i < n and overlap(intervals[i], newInterval):
    #                 newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
    #                 i += 1
    #             ans.append(newInterval)
    #             newI_added = True
    #         elif newInterval[1] < intervals[i][0] and not newI_added:
    #             ans.append(newInterval)
    #             newI_added = True
    #         if i < n:
    #             ans.append(intervals[i])
    #         i += 1

    #     if not newI_added:
    #         ans.append(newInterval)
    #     return ans
