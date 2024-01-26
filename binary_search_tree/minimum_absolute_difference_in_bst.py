from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> Optional[int]:
        min_diff = float("inf")
        prev_node = None

        def inorder(node: Optional[TreeNode]) -> int:
            nonlocal min_diff, prev_node
            if not node:
                return None
            inorder(node.left)
            if prev_node is not None:
                min_diff = min(min_diff, node.val - prev_node)
            prev_node = node.val
            inorder(node.right)

        inorder(root)

        return min_diff

    # def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    #     inorder_nums = []

    #     def inorder(node: Optional[TreeNode]) -> int:
    #         if not node:
    #             return None
    #         inorder(node.left)
    #         inorder_nums.append(node.val)
    #         inorder(node.right)

    #     inorder(root)
    #     min_diff = float("inf")
    #     for i in range(1, len(inorder_nums)):
    #         min_diff = min(min_diff, inorder_nums[i] - inorder_nums[i - 1])

    #     return min_diff
