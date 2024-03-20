from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(permutation) -> None:
            if len(permutation) == len(nums):
                ans.append(permutation[:])
                return None

            for num in nums:
                if num not in seen:
                    seen.add(num)
                    permutation.append(num)
                    backtrack(permutation)
                    permutation.pop()
                    seen.remove(num)

        ans = []
        seen = set()
        backtrack([])
        return ans
