from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == n:
            return [list(range(1, n + 1))]

        def backtrack(idx: int, combination: List[int]) -> None:
            if len(combination) == k:
                ans.append(combination[:])
                return None

            need = k - len(combination)
            for num in range(idx, n + 2 - need):
                combination.append(num)
                backtrack(num + 1, combination)
                combination.pop()

        ans = []
        backtrack(1, [])
        return ans
