from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        p, q = 0, n - 1

        if n == 0:
            return 0

        if n == 1:
            return 1 if nums[0] != val else 0

        while p < q:
            while p < n and nums[p] != val and p < q:
                p += 1
            while q >= 0 and nums[q] == val and q > p - 1:
                q -= 1
            if p < q:
                nums[p], nums[q] = nums[q], nums[p]

        return q + 1
