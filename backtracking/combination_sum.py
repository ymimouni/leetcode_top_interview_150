from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(start: int, rem: int, combination: List[int]) -> None:
            if rem == 0:
                ans.append(list(combination))
                return None
            elif rem < 0:
                return None

            for i in range(start, len(candidates)):
                num = candidates[i]
                if num > rem:
                    break
                combination.append(num)
                helper(i, rem - num, combination)
                combination.pop()

        candidates.sort()
        ans = []
        helper(0, target, [])
        return ans
