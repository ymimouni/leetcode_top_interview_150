class Solution:
    # def lengthOfLastWord(self, s: str) -> int:
    #     n = len(s)
    #     i = n - 1

    #     while i >= 0 and s[i].isspace():
    #         i -= 1

    #     length = 0

    #     while i >= 0 and not s[i].isspace():
    #         length += 1
    #         i -= 1

    #     return length

    # def lengthOfLastWord(self, s: str) -> int:
    #     n = len(s)
    #     i = n - 1
    #     length = 0

    #     while i >= 0:
    #         if not s[i].isspace():
    #             length += 1
    #         elif length > 0:
    #             return length
    #         i -= 1

    #     return length

    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
