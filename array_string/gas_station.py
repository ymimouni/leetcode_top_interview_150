from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        answer = total_gain = curr_gain = 0
        for i in range(n):
            curr_gain += gas[i] - cost[i]
            total_gain += gas[i] - cost[i]

            if curr_gain < 0:
                curr_gain = 0
                answer = i + 1

        return answer if total_gain >= 0 else -1
