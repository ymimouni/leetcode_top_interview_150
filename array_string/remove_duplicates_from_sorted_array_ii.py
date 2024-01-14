from typing import List, Optional


class Solution:
    def removeDuplicates(self, nums: List[Optional[int]]) -> int:
        i = 0
        n = len(nums)

        while i < n - 2:
            if nums[i] == nums[i+1]:
                j = i + 2
                while j < n and nums[i] == nums[j]:
                    nums[j] = None
                    j += 1
                i = j
            else:
                i += 1

        i = 0
        dist = 0
        while i < n:
            if nums[i] is None:
                dist += 1
            else:
                nums[i - dist] = nums[i]
            i += 1

        return n - dist


    # def removeDuplicates(self, nums: List[Optional[int]]) -> int:
    #     i = 0
    #     n = len(nums)

    #     while i < n - 2:
    #         if nums[i] == nums[i+1]:
    #             j = i + 2
    #             while j < n and nums[i] == nums[j]:
    #                 nums[j] = None
    #                 j += 1
    #             i = j
    #         else:
    #             i += 1

    #     i = 0
    #     dist = 0
    #     while i < n:
    #         if nums[i] is None:
    #             dist += 1
    #         else:
    #             nums[i - dist] = nums[i]
    #         i += 1

    #     return n - dist
