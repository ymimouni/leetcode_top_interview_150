class Solution:
    def hammingWeight(self, n: int) -> int:
        h_weight = 0
        while n:
            n &= n - 1
            h_weight += 1
        return h_weight

    # def hammingWeight(self, n: int) -> int:
    #     h_weight = 0
    #     while n:
    #         if n & 1:
    #             h_weight += 1
    #         n >>= 1
    #     return h_weight
