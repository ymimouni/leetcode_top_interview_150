class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n > 0:
            n //= 5
            ans += n
        return ans


# class Solution:
#     def trailingZeroes(self, n: int) -> int:
#         ans = 0
#         multiple = 5
#         while n >= multiple:
#             ans += n // multiple
#             multiple *= 5
#         return ans
