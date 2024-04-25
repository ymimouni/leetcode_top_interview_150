from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot - 1

        return left
