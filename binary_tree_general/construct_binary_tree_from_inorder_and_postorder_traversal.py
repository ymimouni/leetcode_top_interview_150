from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            nonlocal postorder_idx

            if left > right:
                return None

            node_val = postorder[postorder_idx]
            node = TreeNode(val=node_val)
            postorder_idx -= 1
            node.right = array_to_tree(inorder_indices[node_val] + 1, right)
            node.left = array_to_tree(left, inorder_indices[node_val] - 1)

            return node

        n = len(inorder)
        postorder_idx = n - 1
        inorder_indices = {val: idx for (idx, val) in enumerate(inorder)}

        return array_to_tree(0, n - 1)
