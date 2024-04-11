from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        # Binary search.
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left

#     def findPeakElement(self, nums: List[int]) -> int:
#         left, right = 0, len(nums) - 1

#         # Binary search.
#         while left < right:
#             mid = (left + right) // 2

#             if 0 < mid < len(nums) - 1:
#                 if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
#                     return mid
#                 elif  nums[mid - 1] < nums[mid] < nums[mid + 1]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             else:
#                 return mid if nums[mid] > nums[mid + 1] else mid + 1

#         return left
