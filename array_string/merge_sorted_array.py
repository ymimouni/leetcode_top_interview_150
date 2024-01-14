from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = m - 1, n - 1

        for curr in range(m + n - 1, -1, -1):
            if j < 0:
                break
            elif i >= 0 and nums1[i] >= nums2[j]:
                nums1[curr] = nums1[i]
                i -= 1
            else:
                nums1[curr] = nums2[j]
                j -= 1

#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         i, j = m - 1, n - 1
#         curr = m + n - 1

#         while i >= 0 and j >= 0:
#             if nums1[i] >= nums2[j]:
#                 nums1[curr] = nums1[i]
#                 i -= 1
#             else:
#                 nums1[curr] = nums2[j]
#                 j -= 1
#             curr -= 1

#         while j >= 0:
#             nums1[j] = nums2[j]
#             j -= 1
