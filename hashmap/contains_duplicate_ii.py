from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            if i >= k:
                seen.remove(nums[i - k])
            seen.add(num)

        return False
