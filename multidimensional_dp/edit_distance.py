class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prev = [0] * (m + 1)

        for i in range(n + 1):
            curr = [0] * (m + 1)
            for j in range(m + 1):
                if i == 0:
                    curr[j] = j
                elif j == 0:
                    curr[j] = i
                elif word1[j - 1] == word2[i - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(prev[j - 1], prev[j], curr[j - 1])
            prev = curr

        return curr[m]


# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         m, n = len(word1), len(word2)
#         dp = [[0] * (n + 1) for _ in range(m + 1)]

#         for i in range(m + 1):
#             for j in range(n + 1):
#                 if i == 0:
#                     dp[i][j] = j
#                 elif j == 0:
#                     dp[i][j] = i
#                 elif word1[i - 1] == word2[j - 1]:
#                     dp[i][j] = dp[i - 1][j - 1]
#                 else:
#                     dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

#         return dp[m][n]


# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         @lru_cache(maxsize=None)
#         def helper(i: int, j: int) -> int:
#             if i == 0 and j == 0:
#                 return 0
#             elif i == 0:
#                 return j
#             elif j == 0:
#                 return i

#             if word1[i - 1] == word2[j - 1]:
#                 return helper(i - 1, j - 1)
#             else:
#                 return 1 + min(
#                     # Replace.
#                     helper(i - 1, j - 1),
#                     # Insert.
#                     helper(i, j - 1),
#                     # Delete.
#                     helper(i - 1, j)
#                 )

#         return helper(len(word1), len(word2))
