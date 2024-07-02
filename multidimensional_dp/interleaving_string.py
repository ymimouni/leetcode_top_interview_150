from typing import List


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l, m, n = len(s1), len(s2), len(s3)
        if l + m != n:
            return False

        dp = [False] * (m + 1)

        for i in range(l + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i - 1]
                else:
                    dp[j] = (
                            dp[j] and s1[i - 1] == s3[i + j - 1]
                            or dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                    )

        return dp[m]


# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         l, m, n = len(s1), len(s2), len(s3)
#         if l + m != n:
#             return False

#         dp = [[False] * (m + 1) for _ in range(l + 1)]

#         for i in range(l + 1):
#             for j in range(m + 1):
#                 if i == 0 and j == 0:
#                     dp[i][j] = True
#                 elif i == 0:
#                     dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[j - 1]
#                 elif j == 0:
#                     dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i - 1]
#                 else:
#                     dp[i][j] = (
#                         dp[i - 1][j] and s1[i - 1] == s3[i + j - 1] \
#                         or dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
#                         )

#         return dp[l][m]


# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         def dfs(i: int, j: int, k: int) -> bool:
#             if i == len(s1):
#                 return s2[j:] == s3[k:]
#             if j == len(s2):
#                 return s1[i:] == s3[k:]
#             if memo[i][j] >= 0:
#                 return memo[i][j] == 1

#             ans = (
#                 s1[i] == s3[k]
#                 and dfs(i + 1, j, k + 1)
#                 or s2[j] == s3[k]
#                 and dfs(i, j + 1, k + 1)
#                 )
#             memo[i][j] = 1 if ans else 0

#             return ans

#         if len(s1) + len(s2) != len(s3):
#             return False

#         memo = [[-1] * len(s2) for _ in range(len(s1))]

#         return dfs(0, 0, 0)


# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         def helper(i: int, j: int, res: List[str]) -> bool:
#             if i == len(s1) and j == len(s2) and ''.join(res) == s3:
#                 return True

#             ans = False
#             if i < len(s1):
#                 res.append(s1[i])
#                 ans |= helper(i + 1, j, res)
#                 res.pop()
#             if j < len(s2):
#                 res.append(s2[j])
#                 ans |= helper(i, j + 1, res)
#                 res.pop()

#             return ans

#         if len(s1) + len(s2) != len(s3):
#             return False

#         return helper(0, 0, [])

