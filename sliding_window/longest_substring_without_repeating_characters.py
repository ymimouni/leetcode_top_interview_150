class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        last_seen = {}
        for right in range(len(s)):
            if s[right] in last_seen and last_seen[s[right]] >= left:
                left = last_seen[s[right]] + 1
            else:
                ans = max(ans, right - left + 1)
            last_seen[s[right]] = right

        return ans

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         left = right = 0
#         ans = 0
#         chars = set()
#         while right < len(s):
#             while s[right] in chars:
#                 chars.discard(s[left])
#                 left += 1
#             else:
#                 chars.add(s[right])
#                 ans = max(ans, right - left + 1)
#             right += 1

#         return ans
