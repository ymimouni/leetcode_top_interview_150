class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_haystack = len(haystack)
        len_needle = len(needle)

        for i in range(len_haystack - len_needle + 1):
            if haystack[i] == needle[0]:
                for k in range(len_needle):
                    if haystack[i + k] != needle[k]:
                        break
                else:
                    return i

        return -1


# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         m = len(needle)
#         n = len(haystack)
#         if n < m:
#             return -1
#
#         # CONSTANTS
#         RADIX = 26
#         MOD = 1_000_000_033
#         MAX_WEIGHT = 1
#
#         for _ in range(m):
#             MAX_WEIGHT = (MAX_WEIGHT * RADIX) % MOD
#
#         # Function to compute the hash of m-String
#         def hash_value(string):
#             ans = 0
#             factor = 1
#
#             for i in range(m - 1, -1, -1):
#                 ans += ((ord(string[i]) - 97) * (factor)) % MOD
#                 factor = (factor * RADIX) % MOD
#
#             return ans % MOD
#
#         # Compute the hash of needle
#         hash_needle = hash_value(needle)
#
#         # Check for each m-substring of haystack, starting at window_start
#         for window_start in range(n - m + 1):
#             if window_start == 0:
#                 # Compute hash of the First Substring
#                 hash_hay = hash_value(haystack)
#             else:
#                 # Update Hash using Previous Hash Value in O(1)
#                 hash_hay = ((hash_hay * RADIX) % MOD
#                             - ((ord(haystack[window_start - 1]) - 97)
#                                * MAX_WEIGHT) % MOD
#                             + (ord(haystack[window_start + m - 1]) - 97)
#                             + MOD) % MOD
#
#             # If hash matches, Check Character by Character.
#             # Because of Mod, spurious hits can be there.
#             if hash_needle == hash_hay:
#                 for i in range(m):
#                     if needle[i] != haystack[i + window_start]:
#                         break
#                 if i == m - 1:
#                     return window_start
#
#         return -1
#
#
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         m = len(needle)
#         n = len(haystack)
#
#         if n < m:
#             return -1
#
#         # CONSTANTS
#         RADIX_1 = 26
#         MOD_1 = 10 ** 9 + 33
#         MAX_WEIGHT_1 = 1
#         RADIX_2 = 27
#         MOD_2 = 2 ** 31 - 1
#         MAX_WEIGHT_2 = 1
#
#         for _ in range(m):
#             MAX_WEIGHT_1 = (MAX_WEIGHT_1 * RADIX_1) % MOD_1
#             MAX_WEIGHT_2 = (MAX_WEIGHT_2 * RADIX_2) % MOD_2
#
#         # Function to compute hash_pair of m-String
#         def hash_pair(string):
#             hash_1 = hash_2 = 0
#             factor_1 = factor_2 = 1
#             for i in range(m - 1, -1, -1):
#                 hash_1 += ((ord(string[i]) - 97) * factor_1) % MOD_1
#                 factor_1 = (factor_1 * RADIX_1) % MOD_1
#                 hash_2 += ((ord(string[i]) - 97) * factor_2) % MOD_2
#                 factor_2 = (factor_2 * RADIX_2) % MOD_2
#
#             return [hash_1 % MOD_1, hash_2 % MOD_2]
#
#         # Compute hash pairs of needle
#         hash_needle = hash_pair(needle)
#
#         # Check for each m-substring of haystack, starting at window_start
#         for window_start in range(n - m + 1):
#             if window_start == 0:
#                 # Compute hash pairs of the First Substring
#                 hash_hay = hash_pair(haystack)
#             else:
#                 # Update Hash pairs using Previous using O(1) Value
#                 hash_hay[0] = (((hash_hay[0] * RADIX_1) % MOD_1
#                                 - ((ord(haystack[window_start - 1]) - 97)
#                                    * MAX_WEIGHT_1) % MOD_1
#                                 + (ord(haystack[window_start + m - 1]) - 97))
#                                % MOD_1)
#                 hash_hay[1] = (((hash_hay[1] * RADIX_2) % MOD_2
#                                 - ((ord(haystack[window_start - 1]) - 97)
#                                    * MAX_WEIGHT_2) % MOD_2
#                                 + (ord(haystack[window_start + m - 1]) - 97))
#                                % MOD_2)
#
#             # If the hash matches, return immediately.
#             # Probability of Spurious Hit tends to zero
#             if hash_needle == hash_hay:
#                 return window_start
#         return -1
