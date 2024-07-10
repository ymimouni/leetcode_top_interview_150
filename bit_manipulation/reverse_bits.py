class Solution:
    def reverseBits(self, n: int) -> int:
        n = n >> 16 | n << 16
        n = (n & 0xFF00FF00) >> 8 | (n & 0x00FF00FF) << 8
        n = (n & 0xF0F0F0F0) >> 4 | (n & 0x0F0F0F0F) << 4
        n = (n & 0xCCCCCCCC) >> 2 | (n & 0x33333333) << 2
        n = (n & 0xAAAAAAAA) >> 1 | (n & 0x55555555) << 1
        return n

    # def reverseBits(self, n: int) -> int:
    #     ret, power = 0, 31
    #     while n:
    #         ret |= (n & 1) << power
    #         power -= 1
    #         n >>= 1
    #     return ret
