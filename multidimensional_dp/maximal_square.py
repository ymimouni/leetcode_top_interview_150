from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [0] * (n + 1)
        max_len = 0
        prev = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == "1":
                    dp[j] = 1 + min(dp[j], dp[j - 1], prev)
                else:
                    dp[j] = 0
                max_len = max(max_len, dp[j])
                prev = temp

        return max_len * max_len


# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         m, n = len(matrix), len(matrix[0])

#         dp = [[0] * (n + 1) for _ in range(m + 1)]
#         max_len = 0

#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 if matrix[i - 1][j - 1] == "1":
#                     dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
#                 max_len = max(max_len, dp[i][j])

#         return max_len * max_len
