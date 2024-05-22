from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.hi = []
        self.lo = []

    def addNum(self, num: int) -> None:
        heappush(self.hi, num)
        heappush(self.lo, -heappop(self.hi))
        if len(self.hi) < len(self.lo):
            heappush(self.hi, -heappop(self.lo))

    def findMedian(self) -> float:
        if len(self.hi) == len(self.lo):
            return (self.hi[0] - self.lo[0]) / 2
        else:
            return self.hi[0]


# class MedianFinder:

#     def __init__(self):
#         self.nums = []

#     def addNum(self, num: int) -> None:
#         bisect.insort(self.nums, num)

#     def findMedian(self) -> float:
#         n = len(self.nums)
#         if n % 2 == 0:
#             return (self.nums[n // 2] + self.nums[(n - 1) // 2]) / 2
#         else:
#             return self.nums[n // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()