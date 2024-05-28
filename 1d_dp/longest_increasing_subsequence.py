from typing import List

from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        sub = [nums[0]]

        for i in range(1, n):
            num = nums[i]
            if num > sub[-1]:
                sub.append(num)
            else:
                sub[bisect_left(sub, num)] = num

        return len(sub)


# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [1] * n

#         for i in range(n):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j] + 1)

#         return max(dp)
