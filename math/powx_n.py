class Solution:
    def myPow(self, x: float, n: int) -> float:
        if abs(x) < 1e-40: return 0
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        current_product = x
        while n:
            if n % 2:
                ans = ans * current_product
            current_product = current_product * current_product
            n //= 2
        return ans

#     def myPow(self, x: float, n: int) -> float:
#         if n < 0:
#             x = 1 / x
#             n = -n
#         return self.r_pow(x, n)

#     def r_pow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1.0
#         half = self.r_pow(x, n // 2)
#         if n % 2 == 0:
#             return half * half
#         return half * half * x
