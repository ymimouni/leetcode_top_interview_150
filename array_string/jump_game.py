# from functools import lru_cache
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last_pos = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i

        return last_pos == 0

    # def canJump(self, nums: List[int]) -> bool:
    #     n = len(nums)
    #     memo = [None] * n

    #     memo[-1] = True
    #     for i in range(n - 2, -1, -1):
    #         for step in range(1, nums[i] + 1):
    #             if i + step < n and memo[i + step] == True:
    #                 memo[i] = True
    #                 break

    #     return memo[0] == True

    # def canJump(self, nums: List[int]) -> bool:
    #     n = len(nums)

    #     @lru_cache(maxsize=None)
    #     def helper(cur_idx):
    #         if cur_idx == n - 1:
    #             return True
    #         elif cur_idx > n - 1:
    #             return False

    #         for step in range(nums[cur_idx], 0, -1):
    #             if helper(cur_idx + step):
    #                 return True

    #         return False

    #     return helper(0)
