from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = cur = 0

        for num in nums:
            temp = cur
            cur = max(prev + num, cur)
            prev = temp

        return cur
