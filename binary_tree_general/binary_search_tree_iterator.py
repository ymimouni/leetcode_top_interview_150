from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self._gen = self._gen_inorder(root)
        self.cur = next(self._gen)

    def _gen_inorder(self, node: Optional[TreeNode]):
        if not node:
            return None
        yield from self._gen_inorder(node.left)
        yield node.val
        yield from self._gen_inorder(node.right)

    def next(self) -> int:
        temp = self.cur
        try:
            self.cur = next(self._gen)
        except StopIteration:
            self.cur = None
        return temp

    def hasNext(self) -> bool:
        return self.cur is not None

#     def __init__(self, root: Optional[TreeNode]):
#         # Stack for the recursion simulation.
#         self.stack = []

#         self._leftmost_inorder(root)

#     def _leftmost_inorder(self, node):
#         """
#         For a given node, add all the elements in the leftmost branch of the tree under it to the stack.
#         """
#         while node:
#             self.stack.append(node)
#             node = node.left


#     def next(self) -> int:
#         """
#         Return the next smallest number.
#         """

#         # Node at the top of the stack is the next smallest element.
#         topmost_node = self.stack.pop()

#         # Maintain the invariant. If the node has a right child, call the helper function
#         # for the right child.
#         if topmost_node.right:
#             self._leftmost_inorder(topmost_node.right)

#         return topmost_node.val


#     def hasNext(self) -> bool:
#         """
#         @return whether we have a next smallest number.
#         """
#         return len(self.stack) > 0
