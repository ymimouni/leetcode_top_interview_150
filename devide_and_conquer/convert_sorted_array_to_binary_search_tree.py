from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None
            pivot = (left + right) // 2
            node = TreeNode(val=nums[pivot])
            node.left = helper(left, pivot - 1)
            node.right = helper(pivot + 1, right)
            return node

        return helper(0, len(nums) - 1)
