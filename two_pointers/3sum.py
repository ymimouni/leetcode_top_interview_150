from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        seen = set()
        n = len(nums)

        for i, num in enumerate(nums):
            target = -num
            left, right = 0, n - 1
            while left < right:
                if left == i:
                    left += 1
                elif right == i:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    triplet = frozenset([nums[left], nums[right], num])
                    if triplet not in seen:
                        ans.append([nums[left], nums[right], num])
                        seen.add( triplet)
                    left += 1
                    right -= 1

        return ans
