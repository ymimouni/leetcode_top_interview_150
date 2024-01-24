from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_idx

            if left > right:
                return None

            node = TreeNode(val=preorder[preorder_idx])
            preorder_idx += 1
            node.left = array_to_tree(left, inorder_indices[node.val] - 1)
            node.right = array_to_tree(inorder_indices[node.val] + 1, right)

            return node

        preorder_idx = 0
        inorder_indices = {val: idx for (idx, val) in enumerate(inorder)}

        return array_to_tree(0, len(inorder) - 1)
