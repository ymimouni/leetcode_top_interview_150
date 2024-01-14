from typing import List, Union


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(left: int, right: int) -> Union[int, float]:
            if left > right:
                return float("-inf")

            middle = (left + right) // 2
            left_max = helper(left, middle - 1)
            right_max = helper(middle + 1, right)

            curr = left_inc_max = 0
            for idx in range(middle - 1, left - 1, -1):
                curr += nums[idx]
                left_inc_max = max(left_inc_max, curr)

            curr = right_inc_max = 0
            for idx in range(middle + 1, right + 1):
                curr += nums[idx]
                right_inc_max = max(right_inc_max, curr)

            inc_max = left_inc_max + right_inc_max + nums[middle]

            return max(left_max, right_max, inc_max)

        return helper(0, len(nums) - 1)


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         ans = float("-inf")
#         curr = 0

#         for num in nums:
#             curr = max(curr + num, num)
#             ans = max(ans, curr)

#         return ans
