from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if is_first:
                        # Find the left bound.
                        if mid == left or nums[mid - 1] < target:
                            return mid
                        right = mid - 1
                    else:
                        # Find the right bound.
                        if mid == right or nums[mid + 1] > target:
                            return mid
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        left_bound = find_bound(True)
        if left_bound == -1:
            return [-1, -1]
        right_bound = find_bound(False)
        return [left_bound, right_bound]

    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     if not nums:
    #         return [-1, -1]

    #     left, right = 0, len(nums) - 1
    #     while left < right:
    #         mid = (left + right) // 2
    #         if nums[mid] == target:
    #             right = mid
    #         elif nums[mid] < target:
    #             left = mid + 1
    #         else:
    #             right = mid - 1

    #     if nums[left] != target:
    #         return [-1, -1]
    #     left_bound = left

    #     left, right = 0, len(nums) - 1
    #     while left < right:
    #         mid = (left + right) // 2
    #         if nums[mid] == target:
    #             if mid == left:
    #                 if nums[right] != target:
    #                     right -= 1
    #                 else:
    #                     left += 1
    #                     continue
    #             left = mid
    #         elif nums[mid] < target:
    #             left = mid + 1
    #         else:
    #             right = mid - 1

    #     right_bound = right
    #     return [left_bound, right_bound]
