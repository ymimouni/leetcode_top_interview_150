from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max = curr_min = 0
        max_ = nums[0]
        min_ = nums[0]
        sum_ = 0

        for num in nums:
            sum_ += num

            curr_max = max(curr_max, 0) + num
            max_ = max(max_, curr_max)

            curr_min = min(curr_min, 0) + num
            min_ = min(min_, curr_min)

        if sum_ != min_:
            return max(sum_ - min_, max_)

        return max_

    # def maxSubarraySumCircular(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     suffix_max = [0] * n
    #     suffix_sum = suffix_max[n - 1] = nums[n - 1]

    #     for i in range(len(nums) - 2, -1, -1):
    #         suffix_sum += nums[i]
    #         suffix_max[i] = max(suffix_sum, suffix_max[i + 1])

    #     prefix_sum = special_sum = 0
    #     circular_max = special_max = float("-inf")
    #     for i, num in enumerate(nums):
    #         special_sum = max(special_sum + num, num)
    #         special_max = max(special_max, special_sum)

    #         if i + 1 < n:
    #             prefix_sum += num
    #             circular_max = max(circular_max, prefix_sum + suffix_max[i + 1])

    #     return max(circular_max, special_max)
