from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)

        ans = []
        i = 0

        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i] == nums[i + 1] - 1:
                i += 1

            if start != nums[i]:
                ans.append(f"{start}->{nums[i]}")
            else:
                ans.append(f"{start}")
            i += 1

        return ans
