import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(left: int, right: int, pivot_index: int) -> int:
            pivot = nums[pivot_index]

            # Store the pivot at end of the list.
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            store_index = left
            # Find the pivot's final position.
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # Store the pivot in its final position.
            nums[right], nums[store_index] = nums[store_index], nums[right]

            # Return the pivot's final position.
            return store_index

        def select(left: int, right: int, k_smallest: int) -> int:
            if left == right:
                # If the list contains only one element.
                return nums[left]

            # Select a random pivot index.
            pivot_index = random.randint(left, right)

            # Find the pivot position.
            pivot_index = partition(left, right, pivot_index)

            # The pivot is in its final position.
            if pivot_index == k_smallest:
                return nums[pivot_index]
            elif pivot_index > k_smallest:
                # Go left.
                return select(left, pivot_index - 1, k_smallest)
            else:
                # Go right.
                return select(pivot_index + 1, right, k_smallest)

        return select(0, len(nums) - 1, len(nums) - k)

#         def partition(left: int, right: int, pivot_index: int) -> int:
#             pivot = nums[pivot_index]

#             # Move pivot to the end.
#             nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

#             # Move smaller numbers to the left.
#             store_index = left
#             for i in range(left, right):
#                 if nums[i] < pivot:
#                     nums[store_index], nums[i] = nums[i], nums[store_index]
#                     store_index += 1

#             # Move pivot to its final position.
#             nums[right], nums[store_index] = nums[store_index], nums[right]

#             return store_index

#         def select(left: int, right: int, k_smallest: int) -> int:
#             """
#             Returns the k-th smallest element of list with left..right.
#             """
#             if left == right:
#                 # If the list contains only one element.
#                 return nums[left]

#             # Select a random pivot_index.
#             pivot_index = random.randint(left, right)

#             # Find the pivot position after partioning.
#             pivot_index = partition(left, right, pivot_index)

#             # The pivot is in its final position.
#             if k_smallest == pivot_index:
#                 return nums[k_smallest]
#             elif k_smallest < pivot_index:
#                 # Go left.
#                 return select(left, pivot_index - 1, k_smallest)
#             else:
#                 # Go right.
#                 return select(pivot_index + 1, right, k_smallest)

#         return select(0, len(nums) - 1, len(nums) - k)

#         it = iter(nums)
#         ans = list(islice(it, k))

#         heapq.heapify(ans)

#         for num in it:
#             heapq.heappushpop(ans, num)

#         ans.sort()

#         return ans[0]

# return heapq.nlargest(k, nums)[-1]

#         for i in range(len(nums)):
#             nums[i] = -nums[i]

#         heapq.heapify(nums)

#         for _ in range(k - 1):
#             heapq.heappop(nums)

#         return -heapq.heappop(nums)

#         for _ in range(len(nums) - k):
#             heapq.heappop(nums)

#         return heapq.heappop(nums)

#         for num in nums:
#             if len(max_heap) < k:
#                 heapq.heappush(max_heap, num)
#             else:
#                 heapq.heapreplace(max_heap, num)

#         ans = heapq.heappop(max_heap)

#         return ans
