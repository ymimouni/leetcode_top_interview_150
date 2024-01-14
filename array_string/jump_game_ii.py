# from functools import lru_cache
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps, n = 0, len(nums)

        start = end = 0
        i = 0
        while end < n - 1:
            min_jumps += 1
            next_start = end + 1
            next_end = end
            for i in range(start, end + 1):
                if i < n:
                    next_end = max(next_end, i + nums[i])
            start = next_start
            end = next_end

        return min_jumps

    # def jump(self, nums: List[int]) -> int:
    #     min_jumps, n = 0, len(nums)

    #     start = end = 0
    #     for i in range(n):
    #         if i == start:
    #             min_jumps += 1
    #             start = end + 1

    #         end = max(end, i + nums[i])

    #     return min_jumps - 1

    # def jump(self, nums: List[int]) -> int:
    #     n = len(nums)

    #     memo = [float("inf")] * n
    #     memo[n - 1] = 0
    #     for i in range(n - 2, -1, -1):
    #         min_jumps = float("inf")
    #         for step in range(1, nums[i] + 1):
    #             next_i = i + step
    #             if next_i < n:
    #                 min_jumps = min(min_jumps, memo[next_i])

    #         memo[i] = min_jumps + 1

    #     return memo[0]

    # def jump(self, nums: List[int]) -> int:
    #     n = len(nums)

    #     memo = [float("inf")] * n
    #     memo[n - 1] = 0
    #     for i in range(n - 2, -1, -1):
    #         min_jumps = float("inf")
    #         for step in range(1, nums[i] + 1):
    #             next_i = i + step
    #             if next_i < n:
    #                 min_jumps = min(min_jumps, memo[next_i])

    #         memo[i] = min_jumps + 1

    #     return memo[0]

    # def jump(self, nums: List[int]) -> int:
    #     @lru_cache(maxsize=None)
    #     def helper(cur_idx: int) -> int:
    #         n = len(nums)

    #         min_jumps = float("inf")
    #         if cur_idx == n - 1:
    #             return 0
    #         elif cur_idx >= n:
    #             return float("inf")

    #         for step in range(1, nums[cur_idx] + 1):
    #             min_jumps = min(min_jumps, helper(cur_idx + step))

    #         return min_jumps + 1

    #     return helper(0)
