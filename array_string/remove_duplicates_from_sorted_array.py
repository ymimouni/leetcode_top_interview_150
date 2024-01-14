from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        insert_index = 1

        for i in range(1, size):
            if nums[i] != nums[i - 1]:
                nums[insert_index] = nums[i]
                insert_index += 1

        return insert_index
