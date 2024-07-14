class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        rev_x = 0

        while x > rev_x:
            rev_x = 10 * rev_x + x % 10
            x //= 10

        return x == rev_x or x == rev_x // 10

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x_str = str(x)
#         left, right = 0, len(x_str) - 1

#         while left < right:
#             if x_str[left] != x_str[right]:
#                 return False

#             left += 1
#             right -= 1

#         return True
