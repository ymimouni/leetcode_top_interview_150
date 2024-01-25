from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        right_side = []

        def helper(node: TreeNode, level: int) -> None:
            if len(right_side) == level:
                right_side.append(node.val)

            if node.right: helper(node.right, level + 1)
            if node.left: helper(node.left, level + 1)

        helper(root, 0)
        return right_side
