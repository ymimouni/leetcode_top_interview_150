from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0

        for num in nums:
            new_seen_once = (~num & seen_once) | (num & ~seen_once & ~seen_twice)
            seen_twice = (num & seen_once) | (~num & seen_twice)
            seen_once = new_seen_once

        return seen_once


# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         ans = 0

#         for shift in range(32):
#             ones = 0
#             for num in nums:
#                 ones += (num >> shift) & 1
#             ones %= 3
#             ans |= (ones << shift)

#         if ans >= (1 << 31):
#             ans = ans - (1 << 32)

#         return ans
