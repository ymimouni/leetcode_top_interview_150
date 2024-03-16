from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(idx: int, combination: List[str]) -> None:
            if idx == n:
                ans.append(''.join(combination))
                return None

            for c in letters[digits[idx]]:
                combination.append(c)
                backtrack(idx + 1, combination)
                combination.pop()

        ans = []
        backtrack(0, [])

        return ans
