from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 0

        ans = float("inf")
        sum_ = nums[0]
        while left < n and right < n:
            if sum_ >= target:
                ans = min(ans, right - left + 1)
                if left < right:
                    sum_ -= nums[left]
                    left += 1
                else:
                    return 1
            else:
                right += 1
                if right < n:
                    sum_ += nums[right]

        return ans if ans != float("inf") else 0
