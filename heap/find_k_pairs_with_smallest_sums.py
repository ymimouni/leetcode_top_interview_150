from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = [(nums1[0] + nums2[0], (0, 0))]

        ans = []
        for _ in range(k):
            _, (i, j) = heapq.heappop(h)
            ans.append([nums1[i], nums2[j]])

            if j == 0 and i + 1 < len(nums1):
                heapq.heappush(h, (nums1[i + 1] + nums2[j], (i + 1, j)))
            if j + 1 < len(nums2):
                heapq.heappush(h, (nums1[i] + nums2[j + 1], (i, j + 1)))

        return ans


# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         h = [(nums1[0] + nums2[0], (0, 0))]

#         ans = []
#         visited = set()
#         while k > 0 and h:
#             _, (i, j) = heapq.heappop(h)

#             ans.append([nums1[i], nums2[j]])

#             if i < len(nums1) - 1 and (i + 1, j) not in visited:
#                 heapq.heappush(h, (nums1[i + 1] + nums2[j], (i + 1, j)))
#                 visited.add((i + 1, j))
#             if j < len(nums2) - 1 and (i, j + 1) not in visited:
#                 heapq.heappush(h, (nums1[i] + nums2[j + 1], (i, j + 1)))
#                 visited.add((i, j + 1))

#             k -= 1

#         return ans


# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         h = []

#         for num1 in nums1:
#             for num2 in nums2:
#                 if len(h) < k:
#                     heappush(h, (-num1 - num2, [num1, num2]))
#                 else:
#                     heappushpop(h, (-num1 - num2, [num1, num2]))

#         return [heappop(h)[1] for _ in range(k)]
