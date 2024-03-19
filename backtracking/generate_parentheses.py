from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        ans = []
        for left_count in range(n):
            for left_string in self.generateParenthesis(left_count):
                for right_string in self.generateParenthesis(n - left_count - 1):
                    ans.append("(" + left_string + ")" + right_string)

        return ans


# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         def backtrack(opening: int, closing: int, combination: List[str]) -> None:
#             if opening > closing:
#                 return None
#             elif opening == 0 and closing == 0:
#                 ans.append(''.join(combination))
#             elif opening < 0 or closing < 0:
#                 return None

#             combination.append("(")
#             backtrack(opening - 1, closing, combination)
#             combination.pop()

#             combination.append(")")
#             backtrack(opening, closing - 1, combination)
#             combination.pop()

#         ans = []
#         backtrack(n, n, [])
#         return ans
