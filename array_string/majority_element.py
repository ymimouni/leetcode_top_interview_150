from typing import List


class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     count = Counter(nums)
    #     return max(count.keys(), key=count.get)

    # def majorityElement(self, nums: List[int]) -> int:
    #     maj_ele = 0
    #     maj = len(nums) // 2 + 1

    #     bit = 1
    #     for _ in range(32):
    #         count = sum(1 for num in nums if num & bit)
    #         if count >= maj:
    #             maj_ele |= bit

    #         bit <<= 1

    #     return maj_ele

    # def majorityElement(self, nums: List[int]) -> int:
    #     maj = len(nums) // 2 + 1
    #     while True:
    #         candidate = random.choice(nums)
    #         if sum(1 for num in nums if candidate == num) >= maj:
    #             return candidate

    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if candidate == num else -1)

        return candidate
