from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        vu=set()
        for i in nums:
            if i not in vu:
                vu.add(i)
            else:
                vu.remove(i)
        return vu.pop()
