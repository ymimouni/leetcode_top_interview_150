from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        left_max = right_max = 0
        left, right = 0, n - 1
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans

#     def trap(self, height: List[int]) -> int:
#         ans = current = 0
#         stack = []
#         while current < len(height):
#             while stack and height[current] > height[stack[-1]]:
#                 top = stack.pop()
#                 if not stack:
#                     break
#                 distance = current - stack[-1] - 1
#                 bounded_height = min(height[current], height[stack[-1]]) - height[top]
#                 ans += distance * bounded_height
#             stack.append(current)
#             current += 1

#         return ans

#     def trap(self, height: List[int]) -> int:
#         ans = 0

#         n = len(height)
#         left_max= [height[0]] * n
#         right_max = [height[n - 1]] * n
#         for idx in range(1, n):
#             left_max[idx] = max(left_max[idx - 1], height[idx])
#         for idx in range(n - 2, -1, -1):
#             right_max[idx] = max(right_max[idx + 1], height[idx])
#         for idx in range(1, n - 1):
#             ans += min(left_max[idx], right_max[idx]) - height[idx]

#         return ans
